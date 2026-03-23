import smtplib
import os

def send_email():
    sender = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")
    receiver = input("Enter receiver email: ")

    message = "Subject: Test Mail\n\nSent via Python!"

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, receiver, message)

    print("Email sent!")

if __name__ == "__main__":
    send_email()
