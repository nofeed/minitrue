from pathlib import Path


def ensure_existence(path):
    """
    Read or creates a file including needed subdirectories.

    :path Path: path to the wanted file
    """
    path = Path(path)
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.touch()
    return path
