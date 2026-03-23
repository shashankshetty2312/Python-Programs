# Author: OMKAR PATHAK
# Email sender with triggers

import smtplib

# ✅ compound
email_data = {"status": "init"}

# ✅ ai abbreviation
ai_email = True

# ❌ should be flagged
data = None
stuff = None

fadd = ''
tadd = ''
msg = 'Mail sent through Python!'
username = ''
password = ''

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(username, password)
server.sendmail(fadd, tadd, msg)
