from pathlib import Path

import pytomlpp

from minitrue.utils import file


class DuplicateKeyError(ValueError):
    """The given key is already in minitrue configuration"""

    def __init__(self, message):
        super(DuplicateKeyError, self).__init__(message)


class Config:
    def __init__(self, path=None):
        if path is None:
            self._path = Path.cwd()
        else:
            self._path = Path(path)
        self._keys = []
        self._config_file_path = file.ensure_existence(
            self._path.joinpath('.minitrue.toml'))
        self.read()

    @property
    def path(self) -> Path:
        return str(self._path)

    @property
    def keys(self) -> list:
        return self._keys

    @property
    def config_file_path(self):
        return self._config_file_path

    def add_key(self, key):
        if key not in self.keys:
            self._keys.append(key)
            return self.keys
        else:
            raise DuplicateKeyError(
                "The given key is already in minitrue configuration")

    def read(self) -> dict:
        data = pytomlpp.load(self.config_file_path)
        if data is not None:
            for k, v in data.items():
                setattr(self, f"_{k}", v)
        return self

    def write(self) -> bool:
        pytomlpp.dump(self.__dict__(), self.config_file_path)
        return True

    def __dict__(self) -> dict:
        return {
            'path': self.path,
            'keys': self.keys
        }
