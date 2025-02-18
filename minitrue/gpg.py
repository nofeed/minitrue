from typing import Iterator

import gpgme


class KeyChain:
    def __init__(self, key):
        self.context = gpgme.Context()
        if key:
            self._keylist = self.context.keylist(key)
        else:
            self._keylist = self.context.keylist()

    @property
    def keylist(self):
        return self._keylist

    def __iter__(self) -> Iterator:
        for x in self._keylist:
            yield (Key(x))


class Key:
    def __init__(self, key):
        self.key = key
        self._user = self.key.uids[0]
        self._subkeys = self.key.subkeys
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

    def __repr__(self):
        return f"{self.user.name} <{self.user.email}>: {self.fpr}"
