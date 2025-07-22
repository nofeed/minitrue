import typer
from typing import Optional

from .commands import app as commands_app

app = typer.Typer()

app.add_typer(commands_app)


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
