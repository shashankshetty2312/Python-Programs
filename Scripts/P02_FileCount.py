import os

# ❌ BAD naming
search_in_progress = False

def search_file(path, target):
    global isFileSearchStarted
    isFileSearchStarted = True
    
    for root, dirs, files in os.walk(path):
        for file in files:
            if target in file:
                # ❌ BAD naming
                is_file_found = True
                print("Found:", file)
                return
    
    print("Not found")

if __name__ == "__main__":
    PATH = "/home/user/test"  # 🟡 trigger
    search_file(PATH, "data.txt")
