import os
import requests

description_directory = "supplier-data/descriptions"

def parse_text_file(file_dir):
    with open(file_dir, "r") as file:
        result = {}
        result["name"] = file.readline()
        result["weight"] = int(file.readline().split(" ")[0])
        result["description"] = file.readline()
        result["image_name"] = file.readline()
        return result


def __main__():
    for file in os.listdir(description_directory):
        print(parse_text_file(description_directory+"/"+file))


if __name__ == '__main__':
    __main__()
