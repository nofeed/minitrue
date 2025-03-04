from pathlib import Path
from unittest.mock import patch, mock_open

from tests.gpg_util import keys
from minitrue.config import Config
from minitrue.local_config import LocalConfig

fake_config = open(Path(__file__).parent / "resources/dotminitrue", "r").read()

@patch("builtins.open", new_callable=mock_open, read_data=fake_config)
def test_init(mocker, keys: keys):
    path = Path("/example")
    config = Config(path, "FAKEKEY").read()
    local_config = LocalConfig(config)
    assert local_config.path == path.joinpath("config")
