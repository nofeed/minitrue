from collections import OrderedDict
from io import BytesIO
from pathlib import Path
from tempfile import SpooledTemporaryFile

import gpgme
import pytomlpp

from minitrue.utils import file


class DuplicateEntry(ValueError):
    """The given key is already used in the project configuration"""

    def __init__(self, message):
        super(DuplicateEntry, self).__init__(message)


class LocalConfig(OrderedDict):
    def __init__(self, config):
        self._config = config
        self._path = Path(config.path).joinpath('config')
        self._encrypted_config_file_path = file.ensure_existence(
            self._path.joinpath('minitrue.gpg'))
        self._context = gpgme.Context()
        self._recipients = [self._context.get_key(
            key.split(':')[-1]) for key in config.keys]
        self.read()

    @property
    def path(self) -> Path:
        return self._path

    def read(self) -> dict:
        with open(self._encrypted_config_file_path, "rb") as input_file:
            with SpooledTemporaryFile() as output_file:
                try:
                    self._context.decrypt(input_file, output_file)
                    output_file.seek(0)
                    data = pytomlpp.loads(output_file.read())
                    for k, v in data.items():
                        self[k] = v
                except gpgme.GpgmeError:
                    pass
                return self

    def write(self) -> dict:
        with open(self._encrypted_config_file_path, "wb") as output_file:
            content = pytomlpp.dumps(self)
            plaintext_bytes = BytesIO(content.encode('utf8'))
            print(self._recipients)
            self._context.encrypt(
                self._recipients, gpgme.EncryptFlags.ALWAYS_TRUST, plaintext_bytes, output_file)
            return self
