from typer.testing import CliRunner

from minitrue.cli import app
from minitrue.config import Config

from pathlib import Path


runner = CliRunner()
config_path = Path(__file__).parent / ".." / "resources"
name = "VAR"
 

def test_set(mocker):
    Path.unlink(config_path / "config" / "minitrue.gpg")
    mocker.patch("minitrue.config.Config.read", Config(config_path).read)
    result = runner.invoke(app, ["set", name, "VALUE"])
    assert(result.exit_code) == 0
    assert(result.stdout) == f"Variable {name} has been set\n"

def test_duplicated_set(mocker):
    Path.unlink(config_path / "config" / "minitrue.gpg")
    mocker.patch("minitrue.config.Config.read", Config(config_path).read)
    runner.invoke(app, ["set", name, "VALUE"])
    result = runner.invoke(app, ["set", name, "VALUE"])
    assert(result.exit_code) == 0
    assert f"{name} is already set to that value\nVariable {name} couldn't be set" in result.stdout

