import typer

from .init import app as init_app
from .set import app as set_app

app = typer.Typer()

app.add_typer(init_app)
app.add_typer(set_app)
