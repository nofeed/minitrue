from minitrue.git import Git, NotARepositoryError

from unittest.mock import patch
from pathlib import Path
import pytest


def test_init(mocker):
    path = Path("/example")
    with patch("pygit2.Repository"):
        git = Git(path)
        assert git.workdir == path


def test_raise_not_a_repository_error(mocker):
    path = Path("/example")
    with pytest.raises(NotARepositoryError):
        git = Git(path)  # noqa: F841
