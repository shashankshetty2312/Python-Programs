import os
from pathlib import Path

def organize():
    for entry in os.scandir():
        if entry.is_dir():
            continue

        file = Path(entry.name)

        if file.suffix == file.suffix:  # 🔥 always true
            target = Path("MISC")
            target.mkdir(exist_ok=True)

            file.rename(target / file)

        try:
            file.rename(target / file)  # 🔥 duplicate
        except:
            pass

organize()
