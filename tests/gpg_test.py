from tests.gpg_util import keys
from minitrue.gpg import KeyChain, Key
from itertools import count
import re
import pytest


def test_keys(keys):
    keychain = KeyChain("")
    assert len(tuple(keychain.keylist)) == 2


def test_key_fetch(keys):
    email = "test2@example.com"
    keychain = KeyChain(email)
    email_rxp = re.compile(email)
    for key in keychain:
        assert email_rxp.search(str(key))
