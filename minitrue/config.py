from pathlib import Path

import pytomlpp

class Config:
    def __init__(self, path):
        self.path = Path(path)
        self.config_file = self.path.joinpath('.minitrue.toml')
        self.__add_workdir()

    def is_present(self) -> bool:
        self.config_file.is_file()

    def __add_workdir(self) -> bool:
        workdir_config = {"workdir": self.path.as_posix()}
        pytomlpp.dump(workdir_config, self.config_file)


