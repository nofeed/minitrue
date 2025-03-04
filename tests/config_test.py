from pathlib import Path
import re

from minitrue.config import Config


def test_init(mocker):
    path = Path("/example")
    c = Config(path, "FAKEKEY")
    assert c.path == path
    assert c.config_file == path.joinpath(".minitrue.toml")
    assert c.key == "FAKEKEY"


def test_write(tmpdir):
    c = Config(tmpdir, "FAKEKEY")
    config_rxp = re.compile(".minitrue.toml")
    assert c.write()
    assert config_rxp.search(str(c.config_file))
    assert c.config_file.exists()


def test_read(tmpdir):
    c = Config(tmpdir, "FAKEKEY")
    c.write()
    config = c.read()
    assert type(config) is dict
    assert config["key"] == "FAKEKEY"
