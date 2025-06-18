import typer
from rich import print
from rich.prompt import Prompt, Confirm

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
            #update = Confirm.ask(f"Would you like to update the value of {name} to {value}?")
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
        print(f"[green]Variable {name} has been set[/green]")
    else:
        print(f"[bold red]Variable {name} couldn't be set[/bold red]")
