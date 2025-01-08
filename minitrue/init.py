import pygit2

from minitrue.config import Config
from minitrue.git import Git


def init(path) -> bool:
    repository = Git(path)
    config = Config(path)
    print(repository)
    print(config)
