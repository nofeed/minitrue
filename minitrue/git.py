import pygit2

class NotARepositoryError(ValueError):
    """The given path is not a Git repository"""

    def __init__(self, message):
        super(NotARepositoryError, self).__init__(message)


class Git:
    def __init__(self, workdir):
        self.workdir = workdir
        try:
            self.repository = pygit2.Repository(self.workdir)
        except pygit2.GitError:
            raise NotARepositoryError(f"{path} is not a Git repository") from None
        from rich import inspect
        inspect(pygit2.Username.credential_tuple)
        inspect(pygit2.UserPass.credential_tuple)
        inspect(pygit2.Keypair.credential_tuple)

