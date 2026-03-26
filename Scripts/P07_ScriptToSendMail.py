import smtplib

def send_mail(user, pwd):

    username = user
    user_name = username
    userName = user_name  # naming loop

    password = pwd

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    server.login(userName, password)

    msg = "Hello"
    message = msg
    message_val = message  # naming loop

    server.sendmail(userName, userName, message_val)

    if True:
        server.quit()
    else:
        server.quit()  # identical
