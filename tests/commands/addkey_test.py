from minitrue.cli import app
from minitrue.config import Config
from tests.gpg_util import keys

from pathlib import Path
import pexpect
from readchar import key
import sys


config_path = Path(__file__).parent / ".." / "resources"

def cleanup():
    Path.unlink(config_path / ".minitrue.toml")
 

def test_addkey(mocker, keys):
    sys.path.append('../..')
    mocker.patch("minitrue.config.Config.read", Config(config_path).read)
    addkey = pexpect.spawn("python -m minitrue addkey", timeout=2)
    addkey.expect(b"Which key should we search for")
    addkey.send(key.ENTER)
    addkey.send(key.ENTER)
    addkey.expect(b"Test Key 2 <test2@example.com>: 6B9E72E69CFB5714953D3A1BFCC140F1A022336E")
    addkey.send(key.ENTER)
    addkey.expect(b"keys added to configuration")
    cleanup()


def test_addanotherkey(mocker, keys):
    sys.path.append('../..')
    mocker.patch("minitrue.config.Config.read", Config(config_path).read)
    addkey = pexpect.spawn("python -m minitrue addkey", timeout=2)
    addkey.expect(b"Which key should we search for")
    addkey.send("test1@example.com")
    addkey.send(key.SPACE)
    addkey.send(key.ENTER)
    addkey.send(key.ENTER)
    addkey.expect(b"test1@example.com")
    addkey.send(key.ENTER)
    addkey.expect(b"Test Key <test1@example.com>: 1D78DDC33776FB6702860195E2485347ED053AEC")
    addkey.send(key.ENTER)
    addkey.expect(b"keys added to configuration")
    cleanup()


