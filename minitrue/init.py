from minitrue.config import Config
from minitrue.git import Git


def initialize(path) -> bool:
    repository = Git(path)
    config = Config(path)
    print(repository)
    print(config)
