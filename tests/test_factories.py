import pytest

from factories import ServiceFactory
from services import RDAPIPLookupService, GeoIPLookupService

OTHER_SERVICE = 'other_service'


@pytest.fixture
def service_factory():
    return ServiceFactory()


@pytest.mark.parametrize('service, ip_list, instance', [
    ('rdap', ['2.2.2.2', '3.3.3.3'], RDAPIPLookupService),
    ('geoip', ['2.2.2.2', '3.3.3.3'], GeoIPLookupService)
])
def test_service_factory_create_service(service_factory, service, ip_list, instance):
    service = service_factory.create_service(service, ip_list)
    assert isinstance(service, instance)


@pytest.mark.parametrize('service, ip_list', [
    (OTHER_SERVICE, ['2.2.2.2', '3.3.3.3'])
])
def test_service_factory_create_service_will_raise_for_unknown_service(service_factory, service, ip_list):
    with pytest.raises(Exception, match=f'Service {OTHER_SERVICE} not allowed') as e:
        service_factory.create_service(service, ip_list)
