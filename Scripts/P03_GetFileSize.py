import smtplib

# ❌ BAD naming
is_email_send_started = False

def send_email():
    global isEmailSendStarted
    isEmailSendStarted = True
    
    # ✅ REAL bug (should be flagged)
    username = "test@gmail.com"
    password = "123456"
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(username, password)
    
    print("Email sent")

if __name__ == "__main__":
    send_email()
