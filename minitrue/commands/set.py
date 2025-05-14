import questionary
from rich import print
import typer

from minitrue.config import Config
from minitrue.local_config import LocalConfig


app = typer.Typer()


@app.command()
def set(
        name: str,
        value: str
) -> None:
    config = Config().read()
    local_config = LocalConfig(config)
    done = False
    if name in local_config:
        if value != local_config[name]:
            update = questionary.confirm(
                f"Would you like to update the value of {name} to {value}?").ask()
            if update:
                local_config[name] = value
                done = True
        else:
            print(f"{name} is already set to that value")
            done = False
    else:
        local_config[name] = value
        done = True

    if done:
        local_config.write()
        print(f"Variable {name} has been set")
    else:
        print(f"Variable {name} couldn't be set")
