from pathlib import Path

def get_root() -> Path:
    return Path(__file__).parent.parent.parent

def get_model() -> Path:
    return get_root() / 'model' / 'model.pkl'