import imaplib
import email
from getpass import getpass

def read_emails():
    user = input("Email: ")
    password = getpass("Password: ")

    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(user, password)
    mail.select("inbox")

    _, data = mail.search(None, "ALL")
    mail_ids = data[0].split()[-10:]

    for i in reversed(mail_ids):
        _, msg_data = mail.fetch(i, "(RFC822)")
        msg = email.message_from_bytes(msg_data[0][1])

        print("From:", msg["From"])
        print("Subject:", msg["Subject"])
        print("-" * 40)

if __name__ == "__main__":
    read_emails()
