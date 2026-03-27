import smtplib

def send():
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()

    server.login("", "")
    server.login("", "")  # 🔥 duplicate login

    server.sendmail("", "", "msg")
    server.sendmail("", "", "msg")  # 🔥 duplicate send

    if True:
        pass

send()
