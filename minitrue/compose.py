from prompt_toolkit import print_formatted_text as print

from minitrue.config import Config
from minitrue.view import View


def compose() -> bool:
    config = Config()
    print(config.configs)
    for source, destination in config.configs.items():
        View(source, destination, config).compile()
