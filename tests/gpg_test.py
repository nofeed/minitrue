from minitrue.gpg import KeyChain
from tests.gpg_util import keys
import re


def test_keys(keys: keys):
    keychain = KeyChain("")
    assert len(tuple(keychain.keylist)) == 2


def test_key_fetch(keys: keys):
    email = "test2@example.com"
    keychain = KeyChain(email)
    email_rxp = re.compile(email)
    for key in keychain:
        assert email_rxp.search(str(key))
