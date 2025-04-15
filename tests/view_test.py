from pathlib import Path
import os

from minitrue.view import View
from minitrue.config import Config


config_path = Path(__file__).parent / "resources" / "config"


def test_init():
    path = Path(config_path)
    config = Config(str(path)).read()
    for source, destination in config.configs.items():
        view = View(source, destination, config)
        assert view.source == source
        assert view.destination == destination


def test_compile():
    path = Path(config_path)
    config = Config(str(path)).read()
    for source, destination in config.configs.items():
        os.remove(destination)
        View(source, destination, config).compile()
        assert Path(destination).is_file()
