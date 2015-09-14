# -*- coding: UTF-8 -*-
import urllib
from PIL import Image


#GetAuthCodePic
'''
for i in range(50):
    url = 'http://www.zj12580.cn/authCode.svl?type=captcha'
    file("./pic/%04d.png" % i, "wb").write(urllib.urlopen(url).read())

'''

#DetAuthCode



img = Image.open("0021.png")
for i in xrange(120):
    for j in xrange(50):
        pixdata=img.getpixel((i,j))
#       print pixdata
        if(pixdata==(0,0,0,255)):
            for m in xrange(120):
                for n in xrange(50):
                    pixdata1=img.getpixel((m,n))
                    if(pixdata1!=(25,60,170,255) and pixdata1!=(255,255,255,255)):
                        img.putpixel((m,n),(255,255,255,255))
        else:
            img = img.convert("RGBA")
            pixdata = img.load()

for y  in xrange(img.size[1]):
    for x in xrange(img.size[0]):
        if pixdata[x,y][0] < 90:
            pixdata[x,y]=(0,0,0,255)

for y in xrange(img.size[1]):
    for x in xrange(img.size[0]):
        if pixdata[x, y][1] < 136:
            pixdata[x, y] = (0, 0, 0, 255)
for y in xrange(img.size[1]):
    for x in xrange(img.size[0]):
        if pixdata[x, y][2] > 0:
            pixdata[x, y] = (255, 255, 255, 255)
img.save("input-black.png", "PNG")
im_orig = Image.open('input-black.png')
big = im_orig.resize((1000, 500), Image.NEAREST)

