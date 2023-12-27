import json


class Config:
    def __init__(self):
        try:
            with open("environment.json", "r") as environment_file:
                config_data = json.load(environment_file)
            self.ENVIRONMENT = config_data.get("environment")
            self.SERVER_ADDRESS = config_data.get("serverAddress")
            self.SERVER_PORT = config_data.get("port")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON in config file: {e}")


config = Config()