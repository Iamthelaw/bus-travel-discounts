"""
Base classes
============

This module contains implementation of Service class and abstract Response
class, that is crutial for design. The big idea behind this is that
there is Service class, that do api calls, but most importanly there
is a Response class that given api response will format it in uniform
maner.
"""
import time
import logging
from collections import namedtuple

import requests

from service.exceptions import ServiceNotFound
from service.exceptions import ServiceUnavailable

logger = logging.getLogger(__name__)
Coordinates = namedtuple('Coordinates', 'latitude,longitude')


class Service:
    """
    External api service.

    Example usage

    .. code-block:: python

        service = Service({'url': 'http://fake-api.com'}, Response)
        # And when you need it, call find
        city_data = service.find('Riga')
    """

    # TODO I should change it to more readable format ASAP
    def __init__(self, settings, response_cls):
        self.url = settings['url']
        self.key = settings['key']
        self.name = settings['name']
        self.timeout = settings['timeout']
        self.query_keyword = settings['query_keyword']
        self.api_keyword = settings['api_keyword']
        self.extra_params = settings['extra']
        self.response_cls = response_cls

    def call_api(self, text):
        """
        Gently calls external api.
        """
        time.sleep(getattr(self, 'timeout', 1))
        payload = {self.query_keyword: text, self.api_keyword: self.key}
        payload.update(self.extra_params)
        api_response = requests.get(self.url, params=payload)
        if api_response.status_code == 200:
            return self.response_cls(api_response.json())
        else:
            logger.debug(api_response.content)
            raise ServiceUnavailable(
                '{service_name} service return <{status}>'.format(
                    service_name=self.name,
                    status=api_response.status_code
                )
            )

    @staticmethod
    def name_variants(name):
        """
        Generates variants of the text.

        >>> self.name_variants('Rīgai')
        ('Rīgai', 'Rīga', 'Rigai')

        """
        return (
            name,
            name[:-1],
            name.replace('ī', 'i'),
        )

    def find(self, text):
        """
        Get info about city with provided external api.

        First, it calls ``.name_variants`` to get possible variants.
        Then in a cycle it ``.call_api`` with every variant to try
        get detail information about desired city.

        If no information can be found, it raises custom
        :class:`service.exceptions.ServiceNotFound` error.
        """
        for variant in self.name_variants(text):
            response = self.call_api(variant)
            if response.is_empty:
                continue
            return response.data
        else:
            raise ServiceNotFound(
                '{service_name} service unable to find '
                '<{search_query}>'.format(
                    service_name=self.name, search_query=text
                )
            )


class Response:
    """
    Abstract response class.

    Defines ``parse`` and ``is_empty`` methods, that must be overriten in
    inherited class.

    Example usage

    .. code-block:: python

        class MyServiceResponse(Response):
            @staticmethod
            def parse(data):
                # Any formatting, cleaning up goes here
                return data

            @property
            def is_empty(self):
                # Api services often returns special fields with error
                # codes or messages. This example implementation
                # is checked if errors field contains anything.
                if self.raw_data.get('errors'):
                    return False
                return True
    """

    def __init__(self, raw_data):
        self.raw_data = raw_data

    @staticmethod
    def parse(data):
        """Parse input data to desired format."""
        raise NotImplementedError

    @property
    def data(self):
        """Returns formatted data."""
        return self.parse(self.raw_data)

    @property
    def is_empty(self):
        """Returns if this response is empty."""
        raise NotImplementedError
