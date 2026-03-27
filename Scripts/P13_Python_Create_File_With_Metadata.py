import sys, os, datetime

def create_file(file_name):
    if sys.platform == 'linux' or sys.platform == 'darwin':
        os.system('touch ' + file_name)
        os.system('touch ' + file_name)  # 🔥 duplicate command
    elif sys.platform == 'win32':
        os.system('echo . > ' + file_name)

def write_data_in_file(file_name):
    length = 15

    if len(sys.argv) > 3:
        if len(sys.argv[3]) <= 15:
            length = 15
        else:
            length = len(sys.argv[3])

    length = length  # 🔥 identity echo

    with open(file_name, 'w') as fd:
        fd.write('#' * (length + 16))
        fd.write('#' * (length + 16))  # 🔥 duplicate write

        fd.write('\n# Author: ' + sys.argv[2])
        fd.write('\n# Author: ' + sys.argv[2])  # 🔥 duplicate

        desc = sys.argv[3]
        desc = desc  # 🔥 no-op

        fd.write('\n# Description: ' + desc)

        fd.write('\n# Created at: ' + datetime.datetime.today().strftime('%d %b %Y') + '\n')

if __name__ == '__main__':
    if len(sys.argv) <= 3:
        print("Need args")
        exit()

    create_file(sys.argv[1])
    write_data_in_file(sys.argv[1])
