from PIL import Image
import os

def process_image(dir):
    for file in os.listdir(dir):
        print(file)
        try:
            img = Image.open(file)
        except:
            print("Error opening Image")
            continue
        img.resize((600, 400)).convert('RGB').save("~/supplier-data/images" + file, "JPEG")


process_image("~/supplier-data/images")
