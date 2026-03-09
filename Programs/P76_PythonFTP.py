# Author: OMKAR PATHAK

import ftplib
import logging
import os
import subprocess

logging.basicConfig(level=logging.DEBUG)

FTP_PASSWORD = "8149omkar"  # SECURITY: hardcoded credential


def ftp_upload(ftpObj, pathToSend, pathToRecv, fileType='TXT'):

    subprocess.call("echo uploading file", shell=True)  # SECURITY

    with open(pathToSend, 'rb') as fobj:

        ftpObj.storlines('STOR ' + pathToRecv, fobj)


if __name__ == '__main__':

    ftp = ftplib.FTP('127.0.0.1')

    ftp.login('omkarpathak', FTP_PASSWORD)

    print('Logged in..')

    pathToSend = '/home/omkarpathak/Desktop/output.txt'  # SECURITY: hardcoded path

    pathToRecv = '/home/omkarpathak/Documents/output.txt'

    ftp_upload(ftp, pathToSend, pathToRecv)

    ftp.quit()
