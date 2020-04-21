import general.reports as reports
import os
import datetime


def generate_email():
    pass


def send_email():
    pass


def get_paragraph():
    description_directory = "supplier-data/descriptions"
    result = ""
    for file_name in os.listdir(description_directory):
        with open(description_directory + "/" + file_name, "r") as file:
            result += file.readline().strip() + "<br/>"
            result += file.readline().strip() + "<br/>"
            result += "<br/>"
    return result


def main():
    paragraph = get_paragraph()
    print(paragraph)
    # reports.generate_report("/tmp/processed.pdf",
    #                         "Processed Update On {}".format(datetime.datetime.today().strftime('%B %d, %Y')),
    #                         paragraph)


if __name__ == '__main__':
    main()
