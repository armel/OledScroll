#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
OledScroll 
'''

import os
import requests
import sys
import getopt
import settings as s

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


def scroll_message(status, font=None, speed=1):
    author = u"@{0}".format(status.author.screen_name)
    full_text = u"{0}  {1}".format(author, status.text).replace("\n", " ")
    x = device.width

    # First measure the text size
    with canvas(device) as draw:
        w, h = draw.textsize(full_text, font)

    virtual = viewport(device, width=max(device.width, w + x + x), height=max(h, device.height))
    with canvas(virtual) as draw:
        draw.text((x, 0), full_text, font=font, fill="white")
        draw.text((x, 0), author, font=font, fill="yellow")

    i = 0
    while i < x + w:
        virtual.set_position((i, 0))
        i += speed
        time.sleep(0.025)