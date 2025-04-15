
from minitrue.config import Config
from minitrue.view import View


def compose() -> bool:
    config = Config()
    for source, destination in config.configs.items():
        View(source, destination, config).compile()
