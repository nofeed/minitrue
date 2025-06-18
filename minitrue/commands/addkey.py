import inquirer
import typer
from rich import print

from minitrue.keychain import KeyChain
from minitrue.config import Config


app = typer.Typer()


@app.command()
def addkey() -> None:
    questions = [
            inquirer.Text('key', message = "Which key should we search for?", default = None)
            ]
    answer = inquirer.prompt(questions)
    keychain = KeyChain(answer["key"])
    possible_keys = [str(k) for k in keychain]
    questions = [
            inquirer.Checkbox(
                'keys',
                message = "Select the key to add",
                choices = possible_keys,
                carousel = False)
            ]
    answer = inquirer.prompt(questions)
    config = Config()
    [config.add_key(key) for key in answer["keys"]]
    print(config)
    config.write()
    [print(f"[green]{key} added to configuration[/green]") for key in answer]
