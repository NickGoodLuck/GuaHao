
import urllib2
import sys
import chardet
import requests
import time
import urllib
import time
from PIL import Image

url = 'http://www.zj12580.cn/regCaptcha.svl?hospitalId=957101&numId=85199240'
cookies = {'Cookie pair': 'bdshare_firstime=1420946745640; route=3056aea8e2f6f4730e1711d404a6af7e; JSESSIONID=B3BFFF417400F5131E9AAA092BF1EDDC.c; CNZZDATA5472793=cnzz_eid%3D1495464820-1420946454-%26ntime%3D1442231615; Hm_lvt_9e587fb9adef325f8d998c95d459d4f3=1442145113,1442145819,1442230833,1442236249; Hm_lpvt_9e587fb9adef325f8d998c95d459d4f3=1442236282'}
for i in range(50):
    resp = requests.get(url)
    resp = requests.get(url,  cookies=cookies)
    file("./pic/%04d.png" % i, "wb").write(resp.content)
