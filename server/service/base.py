"""Abstract classes for service package."""
import time
import logging
from collections import namedtuple

import requests

from service.exceptions import ServiceNotFound
from service.exceptions import ServiceUnavailable

logger = logging.getLogger(__name__)
Coordinates = namedtuple('Coordinates', 'latitude,longitude')


class Service:
    """Abstract class for external api service."""

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
        """Calls external api service."""
        time.sleep(getattr(self, 'timeout', 1))
        payload = {self.query_keyword: text, self.api_keyword: self.key}
        payload.update(self.extra_params)
        api_response = requests.get(self.url, params=payload)
        if api_response.status_code == 200:
            return self.response_cls(api_response.json())
        else:
            logger.debug(api_response.content)
            raise ServiceUnavailable(
                f'{self.name} service return <{api_response.status_code}>'
            )

    @staticmethod
    def name_variants(name):
        """Returns variants of city name."""
        return (
            name,
            name[:-1],
            name.replace('ī', 'i'),
        )

    def find(self, text):
        """Main method for getting info."""
        for variant in self.name_variants(text):
            response = self.call_api(variant)
            if response.is_empty:
                continue
            return response.data
        else:
            raise ServiceNotFound(
                f'{self.name} service unable to find <{text}>'
            )


class Response:
    """Abstract external api response class."""

    def __init__(self, raw_data):
        self.raw_data = raw_data

    @staticmethod
    def parse(data):
        """Parse input data to desired format."""
        raise NotImplemented

    @property
    def data(self):
        """Returns formatted data."""
        return self.parse(self.raw_data)

    @property
    def is_empty(self):
        """Returns is this response is empty."""
        raise NotImplemented
