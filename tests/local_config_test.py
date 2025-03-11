from pathlib import Path

from tests.gpg_util import keys
from minitrue.config import Config
from minitrue.local_config import LocalConfig

config_path = Path(__file__).parent / "resources"


def test_init(mocker, keys: keys):
    path = Path(config_path)
    config = Config(str(path)).read()
    local_config = LocalConfig(config)
    assert local_config.path.resolve() == path.joinpath("config")


def test_write(mocker, keys: keys):
    path = Path(config_path)
    config = Config(str(path)).read()
    local_config = LocalConfig(config)
    local_config["TEST"] = "TEST"
    assert local_config.write()
