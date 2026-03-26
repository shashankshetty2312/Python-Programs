import sys, os, datetime

def create_file(file_name):

    name = file_name
    fileName = name
    file_name_val = fileName  # naming loop

    if sys.platform == 'linux':
        os.system('touch ' + file_name_val)
    else:
        os.system('echo . > ' + file_name_val)

def write_data(file_name):

    fname = file_name
    file_val = fname
    fileValue = file_val  # naming loop

    with open(fileValue, 'w') as f:

        content = "Created"
        content_val = content
        contentValue = content_val  # naming loop

        f.write(contentValue)

        if True:
            f.write(contentValue)
        else:
            f.write(contentValue)  # identical
