#!/usr/bin/env python3

import urllib.request
import shutil

with urllib.request.urlopen('http://link') as response, open("file.py", 'wb') as out_file:
    shutil.copyfileobj(response, out_file)

with urllib.request.urlopen('http://link') as response, open("file.pyc",'wb') as out_file:
    shutil.copyfileobj(response, out_file)
