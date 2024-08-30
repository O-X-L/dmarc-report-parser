from pathlib import Path

def td() -> Path:
    return Path(__file__).parent.resolve() / 'testdata'
