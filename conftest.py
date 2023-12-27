import pytest

from connection_utils import SocketClient
from config import config


# Initiates the connection to use inside each test
@pytest.fixture(scope="session")
def socket_client():
    client = SocketClient(config.SERVER_ADDRESS, int(config.SERVER_PORT))
    client.connect()
    client.send_data('0A')
    yield client
    client.close()
