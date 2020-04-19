
#!/usr/bin/env python3
import os
from PIL import Image
# im = Image.open("gray-and-black-hive-printed-textile-691710.jpg")
# im.rotate(45).show();
# new_im = im.resize((800,600))
# new_im.save("resized-image.jpg")
#
# print(os.getcwd())
#
# def process_image(dir):
#     for file in os.listdir(dir):
#         try:
#             img = Image.open(file)
#         except:
#             print("Error opening Image");
#         img.rotate(45).resize((128,128)).save(dir+"/icons/rr_"+file)
#
# process_image(os.getcwd())


def process_image(dir):
            for file in os.listdir(dir):
               print(file)
               try:
                   img = Image.open(file)
               except:
                   continue
                   print("Error opening Image");
               img.rotate(90).resize((128,128)).convert('RGB').save("../opt/icons/"+file,"JPEG")


process_image(os.getcwd())


