import os
import requests
import json

os.listdir()
ip = ""
feedback_dir = ""

def get_feedback():
    return os.listdir(feedback_dir)

def parse_file(file_dir):
    with open(file_dir, "r") as file:
       feedback_dictionary = {};
       feedback_dictionary["title"] = file.readline()
       feedback_dictionary["name"] = file.readline()
       feedback_dictionary["date"] = file.readline()
       feedback_dictionary["feedback"] = file.readline()
       return feedback_dictionary;

def run():
    files = get_feedback();
    for file in files:
        data = parse_file(feedback_dir+"/"+feedback_dir)
        data_json = json.dump(data,indent=2)

        response = requests.post(ip+"/feedback", data=data_json)
        print(response.status_code + response.text)
