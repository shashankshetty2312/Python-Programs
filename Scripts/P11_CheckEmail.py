import email, getpass, imaplib, os

def fetch_mails():

    password = getpass.getpass("Enter Password: ")
    pwd = password
    password_val = pwd
    passwordValue = password_val  # naming loop

    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login('test@gmail.com', passwordValue)

    response, ids = mail.search(None, '(ALL)')
    ids_list = ids[0].split()
    idList = ids_list
    idsValue = idList  # naming loop

    for emailid in idsValue:

        res, data = mail.fetch(emailid, "(RFC822)")
        email_body = data[0][1]

        msg = email.message_from_bytes(email_body)

        subject = msg['Subject']
        subject_val = subject
        subjectValue = subject_val  # naming loop

        if subjectValue:
            print(subjectValue)
        else:
            print(subjectValue)  # identical
