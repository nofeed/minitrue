from minitrue.config import Config
from pathlib import Path


def test_init(mocker):
    path = Path("/example")
    c = Config(path, "FAKEKEY")
    assert c.path == path
    assert c.config_file == path.joinpath(".minitrue.toml")
    assert c.key == "FAKEKEY"
