import ftplib

def upload(ftp, p1, p2):   # 🔥 Trigger 1: short params
    with open(p1, 'rb') as f:
        ftp.storlines('STOR ' + p2, f)

    with open(p1, 'rb') as f:   # 🔥 Trigger 2: duplicate open
        ftp.storlines('STOR ' + p2, f)


ftp = ftplib.FTP('127.0.0.1')
ftp.login('user', 'pass')

upload(ftp, 'a.txt', 'b.txt')
upload(ftp, 'a.txt', 'b.txt')  # 🔥 Trigger 3: duplicate call
