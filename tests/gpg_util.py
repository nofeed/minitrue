# This helper is heavily inspired by James Henstridge work, which is
#
# Copyright (C) 2006  James Henstridge
#
# taken from https://github.com/jhenstridge/pygpgme/blob/main/tests/util.py
# and adapted to pytest.
# Thanks to James for the amazing work, it would have taken forever without
# your help  ~ ngw

import os
import shutil
import subprocess
import tempfile
from typing import BinaryIO
import gpgme
import pytest
import pathlib


keydir = os.path.join(os.path.dirname(__file__), 'keys')
gpghome = tempfile.mkdtemp(prefix='tmp.gpghome')


def key(k) -> BinaryIO:
    return open(os.path.join(keydir, k), 'rb')


def import_all_keys() -> list:
    imported_keys: list[str] = list(pathlib.Path(keydir).glob('*.pub'))

    os.environ['GNUPGHOME'] = gpghome
    with open(os.path.join(gpghome, 'gpg.conf'), 'w') as fp:
        fp.write('pinentry-mode loopback\n')
        fp.write('keyserver hkp://keyserver.invalid\n')
    with open(os.path.join(gpghome, 'gpg-agent.conf'), 'w') as fp:
        fp.write('allow-loopback-pinentry\n')
    subprocess.check_call(['gpg-connect-agent', '/bye'],
                          stdout=subprocess.DEVNULL,
                          stderr=subprocess.DEVNULL)

    # import requested keys into the keyring
    ctx = gpgme.Context()
    for k in imported_keys:
        with key(k) as fp:
            ctx.import_(fp)

    return ctx


def tear_down() -> None:
    # May fail if the agent is not currently running.
    subprocess.call(['gpg-connect-agent', 'KILLAGENT', '/bye'],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL)
    del os.environ['GNUPGHOME']
    shutil.rmtree(gpghome, ignore_errors=True)


@pytest.fixture()
def keys():
    ctx = import_all_keys()
    yield ctx.keylist
