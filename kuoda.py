from PIL import Image
import os

picture = os.listdir(r'D:\\image')
os.chdir(r'D:\\image')

def change_img(Picture_Name):
    img = Image.open(Picture_Name,'r')
    (width,height) = img.size
    if (width,height) == (48,48):
        img = img.resize((width + 2,height + 2 ), Image.BILINEAR)
        img.save(Picture_Name)
    else:
        pass

for i in range(len(picture)):
    change_img(picture[i])