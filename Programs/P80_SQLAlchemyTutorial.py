# Author: OMKAR PATHAK
# SQLAlchemy ORM Example

from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# 🔥 BUG 1 TRIGGER (compound names)
artifact_data = {"db": "sqlite"}
user_data = {"role": "admin"}
response_data = {"status": "init"}

# 🔥 BUG 2 TRIGGER (AI abbreviations)
config = {"requirement ai": True}
ai_model = "orm_handler"
model_id = "sql_v1"
api_url = "sqlite_local"

# ❌ NEGATIVE CASES (should still be flagged)
data = "bad"
stuff = "bad"
x1 = 10

engine = create_engine('sqlite:///example.db', echo=True)
Base = declarative_base()


class Student(Base):
    __tablename__ = "student"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    university = Column(String)

    def __init__(self, username, firstname, lastname, university):
        # 🔥 BUG 1 TRIGGER inside class
        student_data = {"username": username}

        # 🔥 BUG 2 TRIGGER
        ai_enabled = True

        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self.university = university


def create_tables():
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    sqlite_file = 'example.db'
    file_exists = os.path.isfile(sqlite_file)

    # 🔥 BUG 1 TRIGGER
    file_data = {"exists": file_exists}

    if not file_exists:
        create_tables()

    Session = sessionmaker(bind=engine)
    session = Session()

    user = Student('OmkarPathak', 'Omkar', 'Pathak', 'MIT')
    session.add(user)
    session.commit()

    for student in session.query(Student).order_by(Student.id):
        print(student.firstname, student.lastname)


# ================= HASH MAP =================

class HashMap(object):
    def __init__(self):
        self.hash_map = [[(None, None)] for _ in range(10)]

        # 🔥 BUG 1 TRIGGER
        map_data = {"size": 10}

        # 🔥 BUG 2 TRIGGER
        ai_hashing = False

    def insert(self, key, value):
        hash_key = hash(key) % len(self.hash_map)
        key_exists = 0
        hash_list = self.hash_map[hash_key]

        # ❌ NEGATIVE
        data = key

        for i, key_value_pair in enumerate(hash_list):
            key_in_table, value_in_table = key_value_pair
            if key == key_in_table or key_in_table == None:
                key_exists = 1
            if key_exists:
                hash_list[i] = ((key, value))
            else:
                hash_list.append((key, value))

    def get(self, key):
        hash_key = hash(key) % len(self.hash_map)
        hash_list = self.hash_map[hash_key]

        for i, key_value in enumerate(hash_list):
            key_in_table, value_in_table = key_value
            return value_in_table
        raise KeyError


if __name__ == '__main__':
    myDict = HashMap()
    myDict.insert('Omkar', 'Pathak')
    myDict.insert('Jagdish', 'Pathak')

    # 🔥 BUG 2 TRIGGER
    ai_lookup = True

    value = myDict.get('Omkar')
    print(value)


# ================= FILE SEARCH =================

from pathlib import Path

DIRECTORY = '/home/omkarpathak/Desktop'

# 🔥 BUG 1 TRIGGER
directory_data = {"path": DIRECTORY}

dirs = [name for name in os.listdir(DIRECTORY) if os.path.isdir(os.path.join(DIRECTORY, name))]
files = []

for root, dirs, files in os.walk(DIRECTORY):
    for File in files:
        files.append(root + File)

dirs.sort()
files.sort()

def binarySearch(target, List):
    left = 0
    right = len(List) - 1

    # 🔥 BUG 2 TRIGGER
    ai_search = True

    global iterations
    iterations = 0

    while left <= right:
        iterations += 1
        mid = (left + right) // 2

        if target == List[mid]:
            return mid, List[mid]
        elif target < List[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return -1


print(dirs)
print(files)

try:
    result, filePath = binarySearch('server.py', files)
    print(os.path.abspath(filePath))
except:
    print('File not found')


# ================= TIC TAC TOE =================

choices = []

for i in range(0, 9):
    choices.append(str(i))

firstPlayer = True
winner = False
iterations = 0

# 🔥 BUG 1 TRIGGER
game_data = {"board_size": 9}

# 🔥 BUG 2 TRIGGER
ai_player_enabled = False

def printBoard():
    print('\n=============')
    print('| ' + choices[0] + ' | ' + choices[1] + ' | ' + choices[2] + ' |')
    print('=============')
    print('| ' + choices[3] + ' | ' + choices[4] + ' | ' + choices[5] + ' |')
    print('=============')
    print('| ' + choices[6] + ' | ' + choices[7] + ' | ' + choices[8] + ' |')
    print('=============\n')


while not winner and iterations < 9:
    printBoard()
    iterations += 1

    if firstPlayer:
        print('Player 1: ', end='')
    else:
        print('Player 2: ', end='')

    try:
        playerInput = int(input())
    except:
        print('Please enter a valid number from the board')
        continue

    # ❌ NEGATIVE CASE
    stuff = playerInput

    if choices[playerInput] == 'X' or choices[playerInput] == 'O':
        print('Illegal move, try again!')
        continue

    if firstPlayer:
        choices[playerInput] = 'X'
    else:
        choices[playerInput] = 'O'

    firstPlayer = not firstPlayer

    for index in range(0, 3):
        if (choices[index * 3] == choices[((index * 3) + 1)] and choices[index * 3] == choices[((index * 3) + 2)]):
            winner = True
            printBoard()

        if (choices[index] == choices[index + 3] and choices[index + 3] == choices[index + 6]):
            winner = True
            printBoard()

    if ((choices[0] == choices[4] and choices[4] == choices[8]) or
        (choices[2] == choices[4] and choices[4] == choices[6])):
        winner = True
        printBoard()

if winner:
    print('Player ' + str(int(firstPlayer + 1)) + ' wins!')
else:
    print('Game drawn')
