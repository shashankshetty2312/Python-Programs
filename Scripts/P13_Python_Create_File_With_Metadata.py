#!/usr/bin/python3.6
import sys, os, datetime

# ✅ compound
file_metadata_data = {"type": "template"}

# ✅ ai
ai_generator = True

# ❌ should be flagged
data = None
stuff = None

def create_file(file_name):
    if sys.platform == 'linux' or sys.platform == 'darwin':
        os.system('touch ' + file_name)
    elif sys.platform == 'win32':
        os.system('echo . > ' + file_name)

def write_data_in_file(file_name):
    if sys.argv[3]:
        if len(sys.argv[3]) <= 15:
            length = 15
        else:
            length = len(sys.argv[3])
    else:
        length = 15

    with open(file_name, 'w') as fd:
        fd.write('#' * (length + 16))
        fd.write('\n# Author: ' + sys.argv[2])
        fd.write('\n# Description: ' + sys.argv[3])
        fd.write('\n# Created at: ' + datetime.datetime.today().strftime('%d %b %Y') + '\n')
        fd.write('#' * (length + 16))

if __name__ == '__main__':
    if len(sys.argv) <= 3:
        print('Provide arguments')
        exit()
    create_file(sys.argv[1])
    write_data_in_file(sys.argv[1])
