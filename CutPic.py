# -*- coding: UTF-8 -*-
from PIL import Image

img = Image.open("test.png")



for x in xrange(160):
    count=0
    for y in xrange(70):
        r,g,b,a = img.getpixel((x,y))
        if(r==0):
            count += 1
    print x,count


"""
img.crop((0,0,43,60)).save("1.png" )
img.crop((44,0,81,60)).save("2.png" )
img.crop((82,0,100,60)).save("3.png" )
img.crop((101,0,129,60)).save("4.png" )
img.crop((130,0,159,60)).save("5.png" )
"""