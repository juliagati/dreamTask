import time
import allure

from test_utils import TestUtils


class TestMicroservice:

    @allure.story('test_basic_initialization')
    def test_basic_initialization(self, socket_client):
        response = socket_client.receive_data()
        TestUtils.log_assert("0" == response, "Initializing Connection Test",
                             "expected response : 0 not equal to received response : " + response)

    @allure.story('test_basic_random_integer')
    def test_basic_random_integer(self, socket_client):
        socket_client.send_data('0B')
        response = socket_client.receive_data()
        random_integer = int(response)
        TestUtils.log_assert(0 <= random_integer <= 10, "Running Process Test",
                             "expected response :" + str(random_integer) + " not equal to received response : "
                             + response)

    @allure.story('test_unknown_command')
    def test_unknown_command(self, socket_client):
        socket_client.send_data('0F')
        response = socket_client.receive_data()
        TestUtils.log_assert(response == "0", "Unknown comment Test",
                             "expected response : 0 not equal to received response : " + str(response))

    @allure.story('test_sequence_of_commands')
    def test_sequence_of_commands(self, socket_client):
        # Send a sequence of commands
        commands = ['0A', '0B', '0A', '0B']
        for command in commands:
            socket_client.send_data(command)
        # Receive the count of commands
        socket_client.send_data('0D')
        response = socket_client.receive_data()
        TestUtils.log_assert(response == "5", "Counting comments Test",
                             "expected response : 5 not equal to received response : " + str(response))

    @allure.story('test_long_running_process_execution')
    def test_long_running_process_execution(self, socket_client):
        socket_client.send_data('0C')
        # Simulate a long-running process by waiting
        time.sleep(5)
        response = socket_client.receive_data()
        TestUtils.log_assert(response == "8", "Running Process Test",
                             "expected response : 8 not equal to received response : " + response)
