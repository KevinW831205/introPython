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

def upload(filename):
    with open(img_directory+"/"+filename,'rb') as opened:
        r = requests.post(url,files={'file':opened})
        print("uploading {} to {} responded with {}".format(filename,url,r.status_code))

# with open('/usr/share/apache2/icons/icon.sheet.png', 'rb') as opened:
#     r = requests.post(url, files={'file': opened})


def __main__():
    for file in os.listdir(img_directory):
        if is_jpeg(file):
            upload(file)


if __name__ == '__main__':
    __main__()
