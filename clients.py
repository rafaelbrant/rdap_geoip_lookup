import requests

from caching import Cache


cache = Cache()


class AbstractClient:
    """Class that represents an abstract client"""

    @property
    def url(self):
        return ''

    def _build_url_for_ip(self, ip: str) -> str:
        return self.url + ip

    def get_data(self, ip: str, name: str) -> requests.Response:
        """Performs a GET on the client URL for the provided key"""
        key = f'{name} {ip}'

        # Using cache to improve performance
        # TODO: We can turn the caching operations into a decorator
        response_from_cache = cache.get_value(key)
        if response_from_cache:
            return response_from_cache

        url = self._build_url_for_ip(ip)
        try:
            response = requests.get(url)
            response.raise_for_status()
            response_json = response.json()
            cache.put(key, response_json)

            return response_json

        except requests.exceptions.HTTPError as error:
            print(error)


class RDAPClient(AbstractClient):
    url = 'https://www.rdap.net/ip/'


class GeoIPCLient(AbstractClient):
    url = 'http://www.geoplugin.net/json.gp?ip='
