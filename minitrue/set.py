from pathlib import Path
from prompt_toolkit import print_formatted_text as print
import questionary

from minitrue.config import Config
from minitrue.local_config import LocalConfig, DuplicateEntry


def set(name: str, value: str, env: str) -> bool:
    path = Path.cwd()
    config = Config(path).read()
    local_config = LocalConfig(config)
    local_config.read()
    try:
        local_config[name] = value
        local_config.write()
    except DuplicateEntry as err:
        if value != local_config._current_local_config[name]:
            update = questionary.confirm(
                f"Would you like to update the value to {value}?").ask()
            if update:
                local_config._current_local_config[name] = value
                local_config.write()
            else:
                print("Thank you, nothing changed")
        else:
            print(format(err))
    finally:
        print(local_config.read())
