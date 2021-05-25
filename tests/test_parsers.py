import pytest

from parsers import IpsParser


EXPECTED_IPS = {'2.2.2.2', '100.100.100.0', '3.3.3.3', '4.4.4.4', '5.5.5.5', '7.7.7.7', '33.22.1.4', '0.0.0.0', '999.999.999.999'}


@pytest.fixture
def ip_parser():
    return IpsParser()


def test_ips_parser_from_txt_file(ip_parser):
    all_ips = ip_parser.from_txt_file('test_file.txt')

    assert set(all_ips) == EXPECTED_IPS
