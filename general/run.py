import os
import requests


description_directory = "supplier-data/descriptions"
ip = ""

def parse_text_file(file_dir,filename):
    with open(file_dir, "r") as file:
        result = {}
        result["name"] = file.readline()
        result["weight"] = int(file.readline().split(" ")[0])
        result["description"] = file.readline()
        result["image_name"] = filename.split(".")[0] + ".jpeg"
        return result


def __main__():
    for file in os.listdir(description_directory):
        data = parse_text_file(description_directory+"/"+file,file)

        response = requests.post(ip+"/fruits",data)
        print("parsed file {} uploading to {}/fruits, responded with {}".format(file,ip,response.status_code))


if __name__ == '__main__':
    __main__()
