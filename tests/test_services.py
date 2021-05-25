import pytest

from clients import AbstractClient
from services import RDAPIPLookupService, GeoIPLookupService

IP_LIST = ['2.2.2.2', '3.3.3.3', '200.200.200.0']


@pytest.fixture
def mock_get_request(mocker):
    return mocker.patch('clients.requests.get')


@pytest.mark.parametrize('service', [
    RDAPIPLookupService(IP_LIST),
    GeoIPLookupService(IP_LIST)
])
def test_rdap_ip_lookup_service_will_call_get(service, mock_get_request):
    service.lookup()
    mock_get_request.assert_called()
