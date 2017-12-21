"""."""
import pytest
import responses

from bs4 import BeautifulSoup

from parser.exceptions import RequestError


@responses.activate
def test_parser_can_make_request(page_url, parser):
    responses.add(responses.GET, page_url, status=200)
    response = parser.harvest(page_url)
    assert response.status_code == 200


@responses.activate
def test_raise_error_if_bad_response(page_url, parser):
    responses.add(responses.GET, page_url, status=404)
    with pytest.raises(RequestError):
        parser.harvest(page_url)


@responses.activate
def test_parser_creates_soup(page_url, html, parser):
    responses.add(
        responses.GET, page_url, body=html, status=200)
    parser.harvest(page_url)
    assert isinstance(parser.soup, BeautifulSoup)
