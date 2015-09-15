
import urllib2
import sys
import chardet
import requests
import time
import urllib
import time
from PIL import Image







img = Image.open("code.png")
img = img.convert("RGBA")
pixdata = img.load()
for y in xrange(img.size[1]):
    for x in xrange(img.size[0]):
        if pixdata[x, y][0] < 90:
            pixdata[x, y] = (0, 0, 0, 255)
for y in xrange(img.size[1]):
    for x in xrange(img.size[0]):
        if pixdata[x, y][1] < 136:
            pixdata[x, y] = (0, 0, 0, 255)
for y in xrange(img.size[1]):
    for x in xrange(img.size[0]):
        if pixdata[x, y][2] > 0:
            pixdata[x, y] = (255, 255, 255, 255)
img.save("test.png", "PNG")
im_orig = Image.open('test.png')
big = im_orig.resize((1000, 500), Image.NEAREST)