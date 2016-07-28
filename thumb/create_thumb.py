#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Hanzhiyun'

from PIL import Image

im = Image.open('test.png')
print(im.format, im.size, im.mode)

im.thumbnail((434, 589))
im.save('thumb_t.jpeg', 'JPEG')
