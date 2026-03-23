import os

def count_files_dirs(path):
    if not os.path.exists(path):
        print("Invalid path!")
        return

    file_count = 0
    dir_count = 0

    for root, dirs, files in os.walk(path):
        file_count += len(files)
        dir_count += len(dirs)

    print(f"Path: {path}")
    print(f"Files: {file_count}")
    print(f"Directories: {dir_count}")
    print(f"Total: {file_count + dir_count}")

if __name__ == "__main__":
    count_files_dirs("/your/path/here")
