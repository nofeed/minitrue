import questionary

from minitrue.config import Config
from minitrue.git import Git, NotARepositoryError
from minitrue.gpg import KeyChain


def initialize(path) -> bool:
    try:
        Git(path)
    except NotARepositoryError:
        path = questionary.text(
            "This is not a Git repository. Where to initialize minitrue? (insert path)").ask()
        initialize(path)

    search_key = questionary.text("Which key should we search for?").ask()
    keychain = KeyChain(search_key)
    keys = [str(k) for k in keychain]
    key = questionary.select("Select the key to use:", choices=keys).ask()
    config = Config(path, key)
    config.write()
