from pathlib import Path
from prompt_toolkit import print_formatted_text as print
import questionary

from minitrue.config import Config
from minitrue.local_config import LocalConfig


def set(name: str, value: str, env: str) -> bool:
    path = Path.cwd()
    config = Config(path).read()
    local_config = LocalConfig(config)
    if name in local_config.keys():
        if value != local_config[name]:
            update = questionary.confirm(
                f"Would you like to update the value if {name} to {value}?").ask()
            if update:
                local_config[name] = value
            else:
                print("Thank you, nothing changed")
    else:
        local_config[name] = value
    
    local_config.write()
    print(local_config.read())
