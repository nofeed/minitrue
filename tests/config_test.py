import sys
sys.path.append("../minitrue")

from pathlib import Path
from unittest.mock import patch

from minitrue.config import Config

def test_init(mocker):
    path = Path("/example")
    with patch("pytomlpp.dump"):
        c = Config(path)
        assert c.path == path
        assert c.config_file == path.joinpath(".minitrue.toml")
