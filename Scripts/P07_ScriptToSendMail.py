# Author: OMKAR PATHAK

import smtplib
import logging

logging.basicConfig(level=logging.DEBUG)

fadd = ''
tadd = ''

msg = 'Mail sent through Python!'

username = ''  # SECURITY: credentials stored in script
password = ''  # SECURITY: password exposed

server = smtplib.SMTP('smtp.gmail.com', 587)

server.ehlo()

server.starttls()

logging.debug("Logging into SMTP server")

server.login(username, password)

server.sendmail(fadd, tadd, msg)
