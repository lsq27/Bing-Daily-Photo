#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''save cn.bing.com's wallpaper'''
import json
import os
import platform
import re
import sys
from StringIO import StringIO

import requests
from PIL import Image

reload(sys)
sys.setdefaultencoding('utf8')


def set_wallpaper(path):
    '''set wallpaper'''
    this_platform = platform.system()
    if this_platform == 'Windows':
        import win32con, win32gui, win32api
        reg_key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,
                                        "Control Panel\\Desktop", 0,
                                        win32con.KEY_SET_VALUE)
        win32api.RegSetValueEx(reg_key, "WallPaper", 0, win32con.REG_SZ, path)
        win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, path,
                                      win32con.SPIF_SENDCHANGE)
    elif this_platform == 'Linux':
        os.system("gsettings set org.gnome.desktop.background picture-uri " +
                  "'file://" + path + "'")


def main():
    '''main'''
    respose = requests.get(
        'http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=8')
    data = json.loads(respose.text)
    for i in range(0, len(data['images'])):
        describe = re.compile(r'(.*) \(').findall(data['images'][i][
            'copyright'])[0]
        date = data['images'][i]['enddate']
        path = os.path.abspath('.') + '/' + date + ' ' + describe + '.jpg'

        if os.path.exists(path) is True:
            break
        else:
            url = 'http://www.bing.com' + data['images'][i]['url']
            image = Image.open(StringIO(requests.get(url).content))
            image.save(path)
            if i == 0:
                set_wallpaper(path)


if __name__ == '__main__':
    main()
