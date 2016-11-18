#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''save cn.bing.com's wallpaper'''
import os
import platform
import re
import sys
from StringIO import StringIO

import requests
from PIL import Image

reload(sys)
sys.setdefaultencoding('utf8')


def get_image_and_describe(url):
    '''得到图片及描述'''
    respose = requests.get(url)
    find_url = re.compile(r'g_img={url: "(\S*.jpg)"')
    find_describe = re.compile(r'class="sc_light" title="(\S*)')
    image_url = find_url.findall(respose.text)
    describe = find_describe.findall(respose.text)
    image = Image.open(StringIO(requests.get(image_url[0]).content))
    return (image, describe[0])


def save_image(image, describe):
    '''保存图片'''
    if os.path.exists(os.path.expanduser('~') + '/图片/' + describe +
                      '.jpg') is False:
        if image.format == 'JPEG':
            image.save(os.path.expanduser('~') + '/图片/' + describe + '.jpg')
        #elif image.format == 'PNG':
        #    image.save(os.path.expanduser('~') + '/图片/' + describe + '.png')


def set_wallpaper(img_path):
    '''设置壁纸'''
    this_platform = platform.system()
    if this_platform == 'Windows':
        import win32api
        import win32con
        import win32gui
        win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, img_path,
                                      win32con.SPIF_SENDCHANGE)
    elif this_platform == 'Linux':
        os.system("gsettings set org.gnome.desktop.background picture-uri " +
                  "'file://" + img_path + "'")
    print 'success'


def main():
    '''main'''
    image, describe = get_image_and_describe('http://cn.bing.com/')
    save_image(image, describe)
    set_wallpaper(os.path.expanduser('~') + '/图片/' + describe + '.jpg')


if __name__ == '__main__':
    main()
