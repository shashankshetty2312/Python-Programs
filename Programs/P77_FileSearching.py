# file_search.py

from pathlib import Path
from typing import List, Optional


class FileSearcher:
    def __init__(self, directory: str):
        self.base_path = Path(directory)

        if not self.base_path.exists():
            raise ValueError("Directory does not exist")

    def get_all_files(self) -> List[str]:
        """Recursively collect all file paths"""
        files = [str(file) for file in self.base_path.rglob("*") if file.is_file()]
        files.sort()
        return files

    def binary_search(self, target: str, files: List[str]) -> Optional[str]:
        """Binary search for filename"""
        left, right = 0, len(files) - 1

        while left <= right:
            mid = (left + right) // 2
            current_file = Path(files[mid]).name

            if current_file == target:
                return files[mid]
            elif target < current_file:
                right = mid - 1
            else:
                left = mid + 1

        return None


def main():
    directory = input("Enter directory path: ").strip()

    searcher = FileSearcher(directory)
    files = searcher.get_all_files()

    target = input("Enter file name to search: ").strip()

    result = searcher.binary_search(target, files)

    if result:
        print("✅ Found:", result)
    else:
        print("❌ File not found")


if __name__ == "__main__":
    main()
