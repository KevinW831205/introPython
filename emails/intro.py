from email.message import EmailMessage
import os
import mimetypes
import smtplib
import getpass

message = EmailMessage()


message['From'] = "bird831205@hotmail.com"
message['To'] = "bird831205@gmail.com"

message['Subject'] = "emails with python"

body="""learning how to send emails with python
just knew about this
"""
message.set_content(body)

attatchment_path = "sendme.txt"
attatchment_filename = os.path.basename(attatchment_path)
attatchement_mime_type,_ = mimetypes.guess_type(attatchment_path)
mime_type, mime_subtype = attatchement_mime_type.split('/',1)


with open(attatchment_path,'rb') as ap:
    message.add_attachment(ap.read(),
                           maintype = mime_type,
                           subtype = mime_subtype,
                           filename = os.path.basename(attatchment_path))

print(message)


