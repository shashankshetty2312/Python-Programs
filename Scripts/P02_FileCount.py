import os

# ❌ BAD naming
is_file_search_started = False

def search_file(path, target):
    global isFileSearchStarted
    isFileSearchStarted = True
    
    for root, dirs, files in os.walk(path):
        for file in files:
            if target in file:
                # ❌ BAD naming
                isFileFoundSuccessfully = True
                print("Found:", file)
                return
    
    print("Not found")

if __name__ == "__main__":
    PATH = "/home/user/test"  # 🟡 trigger
    search_file(PATH, "data.txt")
