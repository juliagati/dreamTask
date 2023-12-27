from config import config


class TestUtils:

    @staticmethod
    def log_assert(comparison, log_message, err_msg=None):
        assert comparison, err_msg
        if config.ENVIRONMENT == 'local':
            print(log_message)
        else:
            pass

