from pathlib import Path
from typing import Optional

import questionary
import typer

app = typer.Typer()


@app.command()
def init(
    path: str = typer.Option(
        Path.cwd(),
        "--path",
        "-p",
        help="Specifies the workdir"
    )
) -> None:
    """Initializes minitrue on a given local repository (default: current)"""
    from minitrue.init import initialize

    initialize(path)


@app.command()
def set(
        name: str,
        value: str,
        env: str = typer.Option(
            "",
            "--env",
            "-e",
            help="Sets the variable on a specific branch (default: current)"
        )
) -> None:
    from minitrue.set import set

    set(name, value, env)


@app.command()
def addkey() -> None:
    from minitrue.addkey import addkey

    addkey()


@app.command()
def addconfig(
        source: Path,
        destination: Path
) -> None:
    from minitrue.addconfig import addconfig

    if not source.exists():
        typer.echo(f"{source} does not exists")
        typer.abort()

    if source.suffix != ".mt":
        typer.echo(f"{source} does not have '.mt' extension")
        confirm = questionary.confirm("Do you want to add it anyway?").ask()
        if not confirm:
            typer.abort()

    if destination.exists():
        typer.echo(f"{destination} will be overritten on compilation.")
        confirm = questionary.confirm("Are you sure?").ask()
        if not confirm:
            typer.abort()

    addconfig(source, destination)


@app.command()
def compose() -> None:
    from minitrue.compose import compose

    compose()


def _version_callback(value: bool) -> None:
    from minitrue import APP_NAME, VERSION
    if value:
        typer.echo(f"{APP_NAME} v{VERSION}")
        raise typer.Exit()


@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    )
) -> None:
    return


if __name__ == "__main__":
    app()
