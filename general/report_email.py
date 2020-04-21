import general.reports as reports
import os
import datetime
import email.message
import mimetypes
import smtplib

import general.emails as emails



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
    message = emails.generate_email("automation@example.com", "student-02-5bece8f61bcc@example.com",
                             "Upload Completed - Online Fruit Store",
                             "All fruits are uploaded to our website successfully. A detailed list is attached to this email",
                             "/tmp/processed.pdf")
    emails.send_email(message)


if __name__ == '__main__':
    main()
