from pathlib import Path
from shutil import copyfile


if __name__ == "__main__":
    output = Path("/output/entry.png")
    output.parent.mkdir(parents=True, exist_ok=True)
    copyfile(Path(__file__).with_name("world-edition.jpg"), output)
