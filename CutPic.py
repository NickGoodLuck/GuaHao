
import os
os.chdir('C:\Python27\Lib\site-packages\pytesseract')

import pytesseract
from PIL import Image
image = Image.open('test.png')
vcode = pytesseract.image_to_string(image)
print vcode