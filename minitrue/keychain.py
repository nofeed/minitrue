from typing import Iterator

import gpgme


class DuplicateKeyError(ValueError):
    """The given key is already in minitrue"""

    def __init__(self, message):
        super(DuplicateKeyError, self).__init__(message)


class KeyChain:
    def __init__(self, key=None):
        self._context = gpgme.Context()
        if key:
            self._keylist = self._context.keylist(key)
        else:
            self._keylist = self._context.keylist()

    @property
    def keylist(self):
        return self._keylist

    def __getitem__(self, key):
        return self._context.get_key(key.split(':')[-1])

    def __iter__(self) -> Iterator:
        for x in self._keylist:
            yield (Key(x))


class Key:
    def __init__(self, key):
        self._key = key
        self._user = self._key.uids[0]
        self._subkeys = self._key.subkeys
        self._fpr = self.subkeys[0].fpr

    @property
    def user(self):
        return self._user

    @property
    def subkeys(self):
        return self._subkeys

    @property
    def fpr(self):
        return self._fpr

    def decrypt(self, input_file, output_file):
        return self._key.decrypt(input_file, output_file)

    def __repr__(self):
        return f"{self.user.name} <{self.user.email}>: {self.fpr}"
