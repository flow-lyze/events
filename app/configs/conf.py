import os
import configparser

from utils.common import Singleton


class Config(metaclass=Singleton):

    CONFIG = {}

    def __init__(self):
        self.__setup_configs()

    def __setup_configs(self):
        prefix = "app/configs"
        config = configparser.ConfigParser()
        config_files = [f"{prefix}/{filename}" for filename in os.listdir(prefix) if filename.endswith(".conf")]
        config.read(config_files)

        for section in config.sections():
            self.CONFIG[section] = dict(config[section])
