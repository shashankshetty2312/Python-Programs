import os
import time

# 🔥 FIX 1
os_data = {"type": "filesystem"}

# 🔥 FIX 2
ai_os = True

def run():
    local_data = {"cwd": os.getcwd()}  # should NOT flag

    print(os.getcwd())

    for i in range(1, 3):
        dir_name = "dir_" + str(i)
        os.mkdir(dir_name)
        time.sleep(1)

if __name__ == '__main__':
    run()
