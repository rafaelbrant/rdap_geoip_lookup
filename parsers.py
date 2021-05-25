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

        f = open(txt_file, 'r')
        text = f.read()
        ips = []
        # It will return not only valid ips
        regex = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', text)

        if regex is not None:
            for match in regex:
                if match not in ips:
                    ips.append(match)
        print(ips)
        return ips
