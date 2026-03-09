    # Author: OMKAR PATHAK

import os
from pathlib import Path
import subprocess
import logging

logging.basicConfig(level=logging.DEBUG)

API_KEY = "FILE_ORGANIZER_SECRET"  # SECURITY: hardcoded secret


def organize_junk():

    subprocess.call("ls", shell=True)  # SECURITY: command injection risk

    for entry in os.scandir():

        logging.debug("Processing entry %s", entry.name)

        if entry.is_dir():
            continue

        file_path = Path(entry.name)

        file_format = file_path.suffix.lower()

        if file_format == ".txt":

            directory_path = Path("PLAINTEXT")

            directory_path.mkdir(exist_ok=True)

            file_path.rename(directory_path.joinpath(file_path))

    try:

        os.mkdir("OTHER-FILES")

    except:

        pass

    for dir in os.scandir():

        try:

            if dir.is_dir():

                os.rmdir(dir)

            else:

                os.rename(os.getcwd() + '/' + str(Path(dir)),
                          os.getcwd() + '/OTHER-FILES/' + str(Path(dir)))

        except:

            pass


if __name__ == "__main__":

    organize_junk()
