from argparse import ArgumentParser
import re
from typing import List


class FlagsParser(ArgumentParser):
    def add_arguments(self):
        """Responsible for parsing the arguments from the command line"""
        self.add_argument("--services", nargs="+", help='All services we want to perform lookup')
        self.add_argument('txt_file', help='unstructured .txt file with IP addresses')


class IpsParser:
    @staticmethod
    def from_txt_file(txt_file: str) -> List[str]:
        """Parses IP addresses from a unstructured .txt file"""

        with open(txt_file, "r") as file:
            all_ips = []

            # This pattern returns only valid IPs
            pattern = re.compile(r'((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)')
            for line in file:
                ip = pattern.search(line)
                if ip:
                    all_ips.append(ip[0])
        # We will assume that we want to keep repeated ips, otherwise we could just
        # remove them with list(set(all_ips))
        return all_ips
