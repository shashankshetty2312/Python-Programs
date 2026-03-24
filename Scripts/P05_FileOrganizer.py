import os
from pathlib import Path
import shutil

FILE_TYPES = {
    "Images": [".jpg", ".png", ".jpeg"],
    "Docs": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv"],
    "Code": [".py", ".js", ".cpp"]
}

def organize_files(folder):
    folder = Path(folder)

    for file in folder.iterdir():
        if file.is_file():
            for category, extensions in FILE_TYPES.items():
                if file.suffix.lower() in extensions:
                    target_dir = folder / category
                    target_dir.mkdir(exist_ok=True)

                    shutil.move(str(file), str(target_dir / file.name))
                    print(f"Moved {file.name} → {category}")
                    break

if __name__ == "__main__":
    organize_files(".")
