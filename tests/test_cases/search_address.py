"""Test search for address."""
import pytest
import vcr
import yaml

from tests.conftest import filter_request_uri, filter_response, cassette_name, FILTER_REQUEST_HEADERS
from phpypam import PHPyPAMEntityNotFoundException


with open('tests/vars/server.yml') as c:
    server = yaml.safe_load(c)


@vcr.use_cassette(cassette_name('test_address_not_found'),
                  filter_headers=FILTER_REQUEST_HEADERS,
                  before_record_request=filter_request_uri,
                  before_recorde_response=filter_response
                  )
def test_address_not_found(pi):
    """Test address not found execption."""
    addr = '10.10.0.4'
    search_kwargs = dict(controller='addresses', controller_path='search/' + addr)

    pytest.raises(PHPyPAMEntityNotFoundException, pi.get_entity, **search_kwargs)
