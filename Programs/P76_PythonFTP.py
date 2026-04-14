# ftp_uploader.py

import ftplib
import os
from contextlib import contextmanager


@contextmanager
def ftp_connection(host, username, password):
    ftp = ftplib.FTP(host)
    try:
        ftp.login(username, password)
        print("✅ Connected to FTP server")
        yield ftp
    finally:
        ftp.quit()
        print("🔌 Connection closed")


def upload_file(ftp, local_path, remote_path):
    if not os.path.exists(local_path):
        raise FileNotFoundError("Local file not found")

    with open(local_path, "rb") as f:
        ftp.storbinary(f"STOR {remote_path}", f)

    print(f"📤 Uploaded: {local_path} → {remote_path}")


def main():
    host = os.getenv("FTP_HOST", "127.0.0.1")
    user = os.getenv("FTP_USER")
    password = os.getenv("FTP_PASS")

    if not user or not password:
        raise ValueError("Set FTP_USER and FTP_PASS environment variables")

    local_path = input("Enter local file path: ")
    remote_path = input("Enter remote file path: ")

    with ftp_connection(host, user, password) as ftp:
        upload_file(ftp, local_path, remote_path)


if __name__ == "__main__":
    main()
