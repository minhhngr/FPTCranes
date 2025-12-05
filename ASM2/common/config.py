from pathlib import Path


class ProjectPath:
    ROOT_PATH = Path(__file__).parent.parent
    DATA_PATH = ROOT_PATH / "data"
