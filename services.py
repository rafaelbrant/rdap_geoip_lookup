from typing import List

from clients import AbstractClient, GeoIPCLient, RDAPClient


class AbstractIPLookupService:
    """Service to perform an IP lookup for a list of ips"""
    def __init__(self, ip_list: List[str]):
        self.ip_list = ip_list

    @property
    def client(self):
        return AbstractClient()

    @property
    def name(self):
        return ''

    def lookup(self):
        """Perform a IP lookup on the provided client"""
        data_list = []
        for ip in self.ip_list:
            data = self.client.get_data(ip, self.name)
            data_list.append(data)
        return data_list


class RDAPIPLookupService(AbstractIPLookupService):
    client = RDAPClient()
    name = 'rdap_service'


class GeoIPLookupService(AbstractIPLookupService):
    client = GeoIPCLient()
    name = 'geoip_service'
