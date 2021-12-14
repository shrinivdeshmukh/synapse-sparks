from sqlalchemy import create_engine
from os import getenv


class Connector:

    def __init__(self, url) -> None:
        self.url = url

    @property
    def engine(self):
        return create_engine(self.url)

    @property
    def destroy(self):
        return self.engine.dispose()
