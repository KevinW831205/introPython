import requests
import os

url = "http://localhost/upload/"
img_directory = "/supplier-data/images"



def is_jpeg(filename):
    try:
        file_parts = filename.split(".")
        return file_parts[len(file_parts)-1] == "jpeg"
    except:
        return False


with open('/usr/share/apache2/icons/icon.sheet.png', 'rb') as opened:
    r = requests.post(url, files={'file': opened})

def __main__():
    for file in os.listdir(img_directory):
        print(file)

if __name__ == '__main__':
    __main__()