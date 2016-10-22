#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''save cn.bing's wallpaper'''
import re
from StringIO import StringIO

import requests
from PIL import Image

RESPOSE = requests.get('http://cn.bing.com/')
FIND_URL = re.compile(r'g_img={url: "(\S*.jpg)"')
FIND_DESCRIBE = re.compile(r'class="sc_light" title="(\S*)')
IMAGE_URL = FIND_URL.findall(RESPOSE.text)
DESCRIBE = FIND_DESCRIBE.findall(RESPOSE.text)
IMAGE = Image.open(StringIO(requests.get(IMAGE_URL[0]).content))

if IMAGE.format == 'JPEG':
    IMAGE.save(DESCRIBE[0] + '.jpg')
elif IMAGE.format == 'PNG':
    IMAGE.save(DESCRIBE[0] + '.png')

if __name__ == '__main__':
    print 1
