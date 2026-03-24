# Author: OMKAR PATHAK (Annotated Version)

import os
from pathlib import Path

# ❌ VIOLATION: Hardcoded path (not portable)
# DIRECTORY = '/home/omkarpathak/Desktop'

# ✅ FIX: Use environment or default
DIRECTORY = os.getenv("SEARCH_DIR", str(Path.home()))


def get_all_files(directory):
    file_list = []

    # ❌ VIOLATION: Original code reused variable 'files' → shadowing bug
    for root, _, files in os.walk(directory):
        for file in files:
            # ❌ VIOLATION: Incorrect path join (root + File)
            # files.append(root + File)

            # ✅ FIX
            file_list.append(os.path.join(root, file))

    return sorted(file_list)


def binary_search(target, file_list):
    left, right = 0, len(file_list) - 1

    # ❌ VIOLATION: Original used global variable 'iterations'
    # global iterations

    while left <= right:
        mid = (left + right) // 2

        filename = os.path.basename(file_list[mid])

        if target == filename:
            return file_list[mid]
        elif target < filename:
            right = mid - 1
        else:
            left = mid + 1

    return None


def main():
    files = get_all_files(DIRECTORY)

    target = "server.py"
    result = binary_search(target, files)

    if result:
        print("Found:", os.path.abspath(result))
    else:
        print("File not found")


if __name__ == "__main__":
    main()
