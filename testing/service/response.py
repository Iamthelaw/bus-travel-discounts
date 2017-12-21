from service.response import OpenCageResponse


def test_response_can_parse_data(geo_api_response):
    response = OpenCageResponse(geo_api_response)
    assert tuple(response.data.keys()) == ('name', 'country', 'latitude', 'longitude')


def test_reponse_can_check_emptiness(geo_api_response):
    response = OpenCageResponse(geo_api_response)
    assert not response.is_empty
