from typing import List

from services import GeoIPLookupService, RDAPIPLookupService


GEOIP_SERVICE_NAME = 'geoip'
RDAP_SERVICE_NAME = 'rdap'


class ServiceFactory:
    @staticmethod
    def create_service(service: str, ip_list: List[str]):
        # if we want to create new services we just need to add it here in the factory.
        if service == GEOIP_SERVICE_NAME:
            return GeoIPLookupService(ip_list)
        if service == RDAP_SERVICE_NAME:
            return RDAPIPLookupService(ip_list)
        else:
            # TODO: Use a specific exception. Using generic Exception is a bad pattern.
            raise Exception(f'Service {service} not allowed')


class ServicesInvoker:
    def __init__(self, ip_list: List[str]):
        self.ip_list = ip_list

    def call_services(self, services: List[str]):
        """Call the services that will return the lookup data"""
        response = dict()

        for service_name in services:
            service = ServiceFactory.create_service(service_name, self.ip_list)
            response[service_name] = service.lookup()
        return response
