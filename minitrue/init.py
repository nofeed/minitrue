from minitrue.config import Config
from minitrue.git import Git
from minitrue.gpg import Gpg


def initialize(path) -> bool:
    repository = Git(path)
    config = Config(path)
    gpg = Gpg()
