import pygit2

from minitrue.config import Config

class NotARepositoryError(ValueError):
    """The given path is not a Git repository"""

    def __init__(self, message):
        super(NotARepositoryError, self).__init__(message)

def init(path) -> bool:
    try:
        repository = pygit2.Repository(path)
    except pygit2.GitError:
        raise NotARepositoryError(f"{path} is not a Git repository") from None
    config = Config(path)
    print(repository)
    print(config)




