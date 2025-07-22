from pathlib import Path
import typer
from rich import print

from minitrue.config import Config
from minitrue.git import Git, NotARepositoryError
from minitrue.keychain import KeyChain


app = typer.Typer()

### BROKEN

@app.command()
def init() -> None:
    """Initializes minitrue on a given local repository (default: current)"""
    path = Path.cwd()
    try:
        Git(path)
    except NotARepositoryError:
        print("This is not a Git repository. minitrue cannot be initialized")

    #search_key = questionary.text("Which key should we search for?").ask()
    keychain = KeyChain(search_key)
    available_keys = [str(k) for k in keychain]
    #selected_keys = questionary.checkbox("Select the keys to use (at least two):", 
    #                                     choices=available_keys).ask()
    config = Config(path)
    for key in selected_keys:
        config.add_key(key)
    config.write()

    print("Configuration has been written in .minitrue")

