from pathlib import Path
from shutil import copyfile


if __name__ == "__main__":
    image = Path(__file__).with_name("world-edition.jpg")
    if not 0 < image.stat().st_size <= 1024 * 1024:
        raise ValueError("The entry image must be nonempty and at most 1 MiB.")

    output = Path("/output/entry.png")
    output.parent.mkdir(parents=True, exist_ok=True)
    copyfile(image, output)
