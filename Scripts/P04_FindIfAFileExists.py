import os

def search_file(filename, path):
    for root, _, files in os.walk(path):
        for file in files:
            if filename.lower() in file.lower():
                print("Found:", os.path.join(root, file))
                return
    print("File not found!")

if __name__ == "__main__":
    search_file("test.txt", "/your/path/here")
