from pathlib import Path

import pytomlpp


class Config:
    def __init__(self, path, key=None):
        self._path = Path(path)
        self._config_file = self.path.joinpath('.minitrue.toml')
        self._key = key

    @property
    def path(self) -> Path:
        return self._path

    @property
    def key(self) -> str:
        return self._key

    @property
    def config_file(self):
        return self._config_file

    def __dict__(self) -> dict:
        return {
            "path": str(self.path),
            "key": self.key
        }

    def read(self) -> dict:
        config = open(self.config_file, "r")
        return pytomlpp.loads(config.read())

    def write(self) -> bool:
        pytomlpp.dump(self.__dict__(), self.config_file)
        return True

