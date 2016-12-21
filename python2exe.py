#!/usr/bin/env python
# -*- coding: utf-8 -*-
from distutils.core import setup

import py2exe

FILE_NAME = "bing_img_cn"  #input("Please input the file name:\n")
setup(
    windows=[{
        "script": FILE_NAME + '.py',
        "icon_resources": [(1, "D:\\IMAGE\\ICON\\8.ico")]
    }],
    options={
        "py2exe": {
            "optimize": 2,
            "compressed": 1,
            "bundle_files": 1,
            "excludes": ['_ssl','_hashlib','doctest', 'pdb', 'unittest', 'difflib', 'inspect' ]
        } 
    },
    zipfile=None,
    version="1",
    description="set bing daily photo as wallpaper",
    name="change wallpaper")
