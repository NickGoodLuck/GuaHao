
import urllib2
import sys
import chardet
import requests
import time
import urllib
import time
from PIL import Image

url = 'http://www.zj12580.cn/regCaptcha.svl?hospitalId=957101&numId=85199240'
cookies = {'Cookie pair': 'bdshare_firstime=1441947667768; route=3056aea8e2f6f4730e1711d404a6af7e; JSESSIONID=8E503FA06D1D46676BFAC0E25E061F41.c; CNZZDATA5472793=cnzz_eid%3D1255717122-1441944651-%26ntime%3D1442302066; Hm_lvt_9e587fb9adef325f8d998c95d459d4f3=1441947668,1441951378,1442196651,1442305535; Hm_lpvt_9e587fb9adef325f8d998c95d459d4f3=1442305554'}
for i in range(50):
    resp = requests.get(url)
    resp = requests.get(url,  cookies=cookies)
    file("./pic/%04d.png" % i, "wb").write(resp.content)
