from typing import Generator

class DataSource:
    def texts(self) -> Generator:
        raise NotImplementedError

    def labels(self) -> Generator:
        raise NotImplementedError