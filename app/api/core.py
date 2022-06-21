from fastapi import FastAPI
from .. utils.common import Singleton


class App(metaclass=Singleton):
    """Singleton App class that allows use the same FastAPI object all over the project"""

    def __init__(self):
        self.server = FastAPI()
