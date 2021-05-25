import pytest

from writer import ResponseWriter

response = {
    'rdap': [{
        "handle": "2.0.0.0 - 2.15.255.255",
        "startAddress": "2.0.0.0",
        "endAddress": "2.15.255.255",
        "ipVersion": "v4",
        "name": "FR-TELECOM-20100712",
        "type": "ALLOCATED PA",
        "country": "FR",
        "etc": "etc"
    }]
}


@pytest.fixture
def response_writer():
    return ResponseWriter(response)


@pytest.fixture
def open_file_mock(mocker):
    return mocker.patch('writer.open')


def test_writer_save_to_json(response_writer, open_file_mock):
    response_writer.save_services_to_json()
    open_file_mock.assert_called()
