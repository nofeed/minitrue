from minitrue.config import Config


def addconfig(source, destination) -> None:
    config = Config()
    config.add_config(source, destination)
    config.write()
