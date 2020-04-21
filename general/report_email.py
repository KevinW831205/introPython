import general.reports as reports
import os
import datetime
import email.message
import mimetypes
import smtplib


def generate_email(sender, recipient, subject, body, attachment_path):
    """Creates an email with an attachement."""
    # Basic Email formatting
    message = email.message.EmailMessage()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(body)

    # Process the attachment and add it to the email
    attachment_filename = os.path.basename(attachment_path)
    mime_type, _ = mimetypes.guess_type(attachment_path)
    mime_type, mime_subtype = mime_type.split('/', 1)

    with open(attachment_path, 'rb') as ap:
        message.add_attachment(ap.read(),
                               maintype=mime_type,
                               subtype=mime_subtype,
                               filename=attachment_filename)

    return message


def send_email(message):
    """Sends the message to the configured SMTP server."""
    mail_server = smtplib.SMTP('localhost')
    mail_server.send_message(message)
    mail_server.quit()


def get_paragraph():
    description_directory = "supplier-data/descriptions"
    result = ""
    for file_name in os.listdir(description_directory):
        with open(description_directory + "/" + file_name, "r") as file:
            result += "name: " + file.readline().strip() + "<br/>"
            result += "weight: " + file.readline().strip() + "<br/>"
            result += "<br/>"
    return result


def main():
    paragraph = get_paragraph()
    reports.generate_report("/tmp/processed.pdf",
                            "Processed Update On {}".format(datetime.datetime.today().strftime('%B %d, %Y')),
                            paragraph)
    message = generate_email("automation@example.com", "student-03-7c6da43177bf@example.com",
                             "Upload Completed - Online Fruit Store",
                             "All fruits are uploaded to our website successfully. A detailed list is attached to this email",
                             "/tmp/processed.pdf")
    send_email(message)


if __name__ == '__main__':
    main()
