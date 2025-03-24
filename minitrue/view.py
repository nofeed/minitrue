from jinja2.sandbox import ImmutableSandboxedEnvironment

from minitrue.local_config import LocalConfig


class SourceNotFoundError(ValueError):
    """The given source does not exist"""

    def __init__(self, message):
        super(SourceNotFoundError, self).__init__(message)


class DestinationExistsError(ValueError):
    """The destination file already exists"""

    def __init__(self, message):
        super(DestinationExistsError, self).__init__(message)


class View:
    def __init__(self, source, destination, config):
        self._source = source
        self._destination = destination
        self._env = ImmutableSandboxedEnvironment()
        self.__locals = LocalConfig(config).read()

    @property
    def source(self):
        try:
            with open(self._source, "r") as s:
                return s.read()
        except FileNotFoundError:
            raise SourceNotFoundError(
                f"{self._source.to_s} cannot be found") from None

    @property
    def destination(self):
        return self._destination

    def compile(self, force=False):
        with open(self._destination, "w") as d:
            compiled = self._env.from_string(self.source).render(self.__locals)
            d.write(compiled)
