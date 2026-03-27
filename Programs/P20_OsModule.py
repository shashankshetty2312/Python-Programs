import os

def create():
    path = os.getcwd()             # 🎯 trigger
    os.mkdir('newDir')             # 🎯 trigger
    return path                    # 🎯 trigger


print(create())
