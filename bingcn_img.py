#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''save cn.bing's wallpaper'''
import os
import re
from StringIO import StringIO

import requests
from PIL import Image


def get_image(url):
    '''得到图片'''
    respose = requests.get(url)
    find_url = re.compile(r'g_img={url: "(\S*.jpg)"')
    find_describe = re.compile(r'class="sc_light" title="(\S*)')
    image_url = find_url.findall(respose.text)
    describe = find_describe.findall(respose.text)
    image = Image.open(StringIO(requests.get(image_url[0]).content))
    return (image, describe[0])


def save_image(image, describe):
    if image.format == 'JPEG':
        image.save(os.path.expanduser('~') + u'/图片/' + describe + '.jpg')
    elif image.format == 'PNG':
        image.save(os.path.expanduser('~') + u'/图片/' + describe + '.png')


def main():
    image, describe = get_image('http://cn.bing.com/')
    save_image(image, describe)


if __name__ == '__main__':
    main()
