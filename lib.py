#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
OledScroll 
'''

import os
import requests
import sys
import getopt
import time
import settings as s
from luma.core.render import canvas
from luma.core import legacy
from luma.core.virtual import viewport

from PIL import ImageFont

#font = ImageFont.truetype('./fonts/7x5.ttf', 8)           # Text font
font = ImageFont.truetype('./fonts/rounded_led_board.ttf', 20)

# Usage
def usage():
    print 'Usage: RRFDisplay.py [options ...]'
    print
    print '--help               this help'
    print
    print 'Interface settings :'
    print '  --interface        set interface (default=i2c, choose between [i2c, spi])'
    print '  --i2c-port         set i2c port (default=0)'
    print '  --i2c-address      set i2c address (default=0x3C)'
    print
    print 'Display settings :'
    print '  --display          set display (default=sh1106, choose between [sh1106, ssd1306, ssd1327, ssd1351, st7735])'
    print '  --display-width    set display width (default=128)'
    print '  --display-height   set display height (default=64)'
    print
    print '88 & 73 from F4HWN Armel'


def scroll_message(status, font=None, speed=4):
    full_text = status
    x = s.device.width

    # First measure the text size
    with canvas(s.device) as draw:
        w, h = draw.textsize(full_text, font=font)

    virtual = viewport(s.device, width=max(s.device.width, w + x + x), height=max(h, s.device.height))
    with canvas(virtual) as draw:
        draw.text((x, 0), full_text, font=font, fill="white")

    i = 0
    while i < x + w:
        virtual.set_position((i, 0))
        i += speed
        time.sleep(0.1)
