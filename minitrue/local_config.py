from collections import OrderedDict
from io import BytesIO
from pathlib import Path
from tempfile import SpooledTemporaryFile

import gpgme
import pytomlpp


class DuplicateEntry(ValueError):
    """The given key is already used in the project configuration"""

    def __init__(self, message):
        super(DuplicateEntry, self).__init__(message)


class LocalConfig(OrderedDict):
    def __init__(self, config):
        self._config = config
        self._path = Path(config["path"]).joinpath('config')
        self._encrypted_config_file_path = self._path.joinpath('minitrue.gpg')
        self._context = gpgme.Context()
        self._key = self._context.get_key(config['key'].split(':')[-1])
        self.read()

    @property
    def path(self) -> Path:
        return self._path

    def __dict__(self):
        return self._current_local_config

    def __iter__(self):
        yield dict(self._current_local_config)

    def __getitem__(self, k):
        return self._current_local_config[k]

    def __setitem__(self, k, v):
        if k in self._current_local_config:
            raise DuplicateEntry(
                f"{k} is already set to {
                    self._current_local_config[k]}")
        else:
            self._current_local_config[k] = v
            return self._current_local_config[k]

    def read(self) -> dict:
        with open(self._encrypted_config_file_path, "rb") as input_file:
            with SpooledTemporaryFile() as output_file:
                self._context.decrypt(input_file, output_file)
                output_file.seek(0)
                self._current_local_config = pytomlpp.loads(output_file.read())
                return self._current_local_config

    def write(self) -> dict:
        with open(self._encrypted_config_file_path, "wb") as output_file:
            content = pytomlpp.dumps(self._current_local_config)
            plaintext_bytes = BytesIO(content.encode('utf8'))
            self._context.encrypt([self._key], 0, plaintext_bytes, output_file)
            return self._current_local_config
