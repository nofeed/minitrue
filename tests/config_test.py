import re
from pathlib import Path

from minitrue.config import Config


def test_init(tmpdir):
    c = Config(str(tmpdir))
    assert c.path == str(tmpdir)
    assert c.config_file_path == Path(tmpdir).joinpath(".minitrue.toml")


def test_write(tmpdir):
    c = Config(str(tmpdir))
    config_rxp = re.compile(".minitrue.toml")
    assert c.write()
    assert config_rxp.search(str(c.config_file_path))
    assert c.config_file_path.exists()


def test_add_key(tmpdir):
    c = Config(str(tmpdir))
    assert c.write()
    config = c.read()
    assert config.keys == []
    c.add_key("FAKEKEY")
    assert config.keys == ["FAKEKEY"]
    c.add_key("SECOND_FAKEKEY")
    assert c.write()
    config = c.read()
    assert config.keys == ["FAKEKEY", "SECOND_FAKEKEY"]
