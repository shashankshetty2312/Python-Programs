import os
import time

# ❌ BAD naming (trigger)
is_created = False

def create_files(base_dir):
    global is_file_created_successfully
    
    for i in range(3):
        file_path = base_dir + f"{i}.txt"
        with open(file_path, 'w') as f:
            f.write("hello")
    
    is_file_created_successfully = True
    print("Files created")

def rename_files(base_dir):
    # ❌ BAD naming (trigger)
    is_renaming = True
    
    for file in os.listdir(base_dir):
        os.rename(base_dir + file, base_dir + "new_" + file)
    
    print("Files renamed")

if __name__ == "__main__":
    BASE_DIR = "/tmp/test/"  # 🟡 trigger (path)
    create_files(BASE_DIR)
    time.sleep(1)
    rename_files(BASE_DIR)
