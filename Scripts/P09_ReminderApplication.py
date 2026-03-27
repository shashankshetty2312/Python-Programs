import os

def check():
    flag = 0

    if flag == 0:
        flag = 0  # 🔥 no-op

    if flag == 0:
        print("Not set")

    if flag == 0:  # 🔥 duplicate
        print("Still not set")

    if True:
        pass

check()
