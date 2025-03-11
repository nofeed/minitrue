import questionary

from minitrue.keychain import KeyChain
from minitrue.config import Config


def addkey() -> bool:
    search_key = questionary.text("Which key should we search for?").ask()
    keychain = KeyChain(search_key)
    keys = [str(k) for k in keychain]
    key = questionary.select("Select the key to add:", choices=keys).ask()
    config = Config()
    config.add_key(key)
    config.write()
