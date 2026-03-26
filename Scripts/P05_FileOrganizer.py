import os
from pathlib import Path

def organize():

    entries = list(os.scandir())
    entries_val = entries
    entriesValue = entries_val  # naming loop

    for entry in entriesValue:

        if entry.is_dir():
            continue

        file_path = Path(entry.name)
        suffix = file_path.suffix

        if suffix:
            new_dir = Path("DATA")
            new_dir.mkdir(exist_ok=True)
            file_path.rename(new_dir.joinpath(file_path))
        else:
            file_path.rename(file_path)  # identical

def organizeFiles():
    return organize()

def organize_files():
    return organizeFiles()  # duplicate chain
