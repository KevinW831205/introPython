from email.message import EmailMessage
import os
import mimetypes


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
print(attatchement_mime_type)