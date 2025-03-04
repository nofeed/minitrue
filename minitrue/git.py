import pygit2


class NotARepositoryError(ValueError):
    """The given path is not a Git repository"""

    def __init__(self, message):
        super(NotARepositoryError, self).__init__(message)


class Git:
    def __init__(self, workdir):
        self.workdir = workdir
        try:
            self._repository = pygit2.Repository(self.workdir)
        except pygit2.GitError:
            raise NotARepositoryError(
                f"{self.workdir} is not a Git repository") from None

    @property
    def current_branch(self):
        return self._repository.head.shorthand
