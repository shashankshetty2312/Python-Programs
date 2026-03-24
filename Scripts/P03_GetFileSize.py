import os

def get_folder_size(path):
    total_size = 0

    for root, _, files in os.walk(path):
        for file in files:
            try:
                file_path = os.path.join(root, file)
                total_size += os.path.getsize(file_path)
            except:
                continue

    return total_size


def convert_size(size):
    for unit in ['Bytes', 'KB', 'MB', 'GB']:
        if size < 1024:
            return f"{round(size, 2)} {unit}"
        size /= 1024


if __name__ == "__main__":
    path = "/your/path/here"
    size = get_folder_size(path)
    print("Folder Size:", convert_size(size))
