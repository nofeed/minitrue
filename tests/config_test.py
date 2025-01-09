from minitrue.config import Config
from unittest.mock import patch
from pathlib import Path


def test_init(mocker):
    path = Path("/example")
    with patch("pytomlpp.dump"):
        c = Config(path)
        assert c.path == path
        assert c.config_file == path.joinpath(".minitrue.toml")
