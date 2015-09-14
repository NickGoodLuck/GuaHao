# -*- coding: UTF-8 -*-
import urllib2
import sys
import chardet
import requests
import time
import urllib
import time
from PIL import Image

"""
#GetAuthCodePic#
url = 'http://www.zj12580.cn/regCaptcha.svl?hospitalId=957101&numId=85199240'
cookies = {'Cookie pair': 'bdshare_firstime=1441947667768; route=549c62a15223beac1a34a8bace2dcc64; JSESSIONID=43AED5111AF592DFC1024CC57D4DF854.b; CNZZDATA5472793=cnzz_eid%3D1255717122-1441944651-%26ntime%3D1442214074; Hm_lvt_9e587fb9adef325f8d998c95d459d4f3=1441947668,1441951378,1442196651; Hm_lpvt_9e587fb9adef325f8d998c95d459d4f3=1442217456'}
for i in range(50):
    resp = requests.get(url)
    resp = requests.get(url,  cookies=cookies)
    file("./pic/%04d.png" % i, "wb").write(resp.content)

"""




#DetAuthCode



img = Image.open("0000.png")
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