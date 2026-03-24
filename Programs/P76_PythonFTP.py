# 🔥 IDENTITY TRIGGERS (file open duplication)
path = "file.txt"

f1 = open(path, 'w')
f2 = open(path, 'w')  # duplicate operation

f1.close()
f2.close()


# ORIGINAL CODE
import ftplib

def ftp_upload(ftpObj, pathToSend, pathToRecv):
    with open(pathToSend, 'rb') as fobj:
        ftpObj.storlines('STOR ' + pathToRecv, fobj)
