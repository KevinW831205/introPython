from email.message import EmailMessage

message = EmailMessage()


message['From'] = "bird831205@hotmail.com"
message['To'] = "bird831205@gmail.com"

message['Subject'] = "emails with python"

body="""learning how to send emails with python
just knew about this
"""
message.set_content(body)

print(message)