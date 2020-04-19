import os
import requests

os.listdir()
ip = ""

def get_feedback():
    return os.listdir("/data/feedback")

def parse_file(file_dir):
    with open(file_dir, "r") as file:
       feedback_dictionary = {};
       feedback_dictionary["title"] = file.readline()
       feedback_dictionary["name"] = file.readline()
       feedback_dictionary["date"] = file.readline()
       feedback_dictionary["feedback"] = file.readline()
       return feedback_dictionary;

