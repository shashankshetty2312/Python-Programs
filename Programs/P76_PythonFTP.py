import ftplib

def ftpUploadHandler(ftpObj, pathToSendFile, pathToReceiveFile):
    isFileUploadStartedSuccessful = True
    isFileUploadStartSuccessful = True  # ❌ escalation

    previousView = "ftp_screen"  # ❌

    with open(pathToSendFile, 'rb') as fileObj:
        ftpObj.storlines('STOR ' + pathToReceiveFile, fileObj)


def ftpConnectionManager():
    mfApi = "ftp_api"  # ❌

    isConnectionDone = False  # ❌
    isConnectionCompleted = False  # ❌ escalation

    ftp = ftplib.FTP('127.0.0.1')
    ftp.login('user', 'password')

    return ftp


if __name__ == "__main__":
    ftp = ftpConnectionManager()
    ftp.quit()
