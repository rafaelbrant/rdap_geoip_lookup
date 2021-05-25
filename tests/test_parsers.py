import pytest

from parsers import IpsParser


@pytest.fixture
def ip_parser():
    return IpsParser()


def test_ips_parser_from_txt_file(ip_parser):
    all_ips = ip_parser.from_txt_file('test_file.txt')
    assert set(all_ips) == {'2.2.2.2', '3.3.3.3', '4.4.4.4', '7.7.7.7', '2.2.2.2'}