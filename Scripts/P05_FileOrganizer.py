import os
from pathlib import Path

# ✅ compound
file_data = {"type": "image"}

# ✅ ai usage
ai_organizer = True

# ❌ should be flagged
data = None
stuff = None

DIRECTORIES = {
    "IMAGES": [".jpg", ".png"],
    "DOCS": [".txt", ".pdf"]
}

FILE_FORMATS = {
    ext: folder for folder, exts in DIRECTORIES.items() for ext in exts
}


def organize():
    for entry in os.scandir():
        if entry.is_dir():
            continue
        file_path = Path(entry.name)
        file_format = file_path.suffix.lower()
        if file_format in FILE_FORMATS:
            directory_path = Path(FILE_FORMATS[file_format])
            directory_path.mkdir(exist_ok=True)
            file_path.rename(directory_path.joinpath(file_path))


if __name__ == "__main__":
    organize()
