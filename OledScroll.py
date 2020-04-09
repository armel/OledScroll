#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
OledScroll 
'''

import settings as s
import display as d
import lib as l

import time
import sys
import getopt
import configparser as cp

from luma.core.interface.serial import i2c, spi
from luma.core.render import canvas

from luma.oled.device import sh1106
from luma.oled.device import ssd1306
from luma.oled.device import ssd1327
from luma.oled.device import ssd1351
from luma.lcd.device  import st7735

def main(argv):

    # Check and get arguments
    try:
        options, remainder = getopt.getopt(argv, '', ['help', 'interface=', 'i2c-port=', 'i2c-address=', 'display=', 'display-width=', 'display-height=', 'display-theme=', 'follow=', 'refresh=', 'latitude=', 'longitude='])
    except getopt.GetoptError:
        l.usage()
        sys.exit(2)
    for opt, arg in options:
        if opt == '--help':
            l.usage()
            sys.exit()
        elif opt in ('--interface'):
            if arg not in ['i2c', 'spi']:
                print 'Unknown interface type (choose between \'i2c\' and \'spi\')'
                sys.exit()
            s.interface = arg
        elif opt in ('--i2c-port'):
            s.i2c_port = int(arg)
        elif opt in ('--i2c-address'):
            s.i2c_address = int(arg, 16)
        elif opt in ('--display'):
            if arg not in ['sh1106', 'ssd1306', 'ssd1327', 'ssd1351', 'st7735']:
                print 'Unknown display type (choose between \'sh1106\', \'ssd1306\',  \'ssd1327\', \'ssd1351\' and \'st7735\')'
                sys.exit()
            s.display = arg
        elif opt in ('--display-width'):
            s.display_width = int(arg)
        elif opt in ('--display-height'):
            s.display_height = int(arg)
        elif opt in ('--follow'):
            if arg in ['RRF', 'TECHNIQUE', 'INTERNATIONAL', 'LOCAL', 'BAVARDAGE', 'FON']:
                s.room_current = arg
            else:
                s.room_current = 'RRF'
                tmp = l.scan(arg)
                if tmp is False:
                    s.room_current = 'RRF'
                else:
                    s.room_current = tmp
                    s.callsign = arg
                    s.scan = True
        elif opt in ('--refresh'):
            s.refresh = float(arg)
        elif opt in ('--latitude'):
            s.latitude = float(arg)
        elif opt in ('--longitude'):
            s.longitude = float(arg)
        elif opt in ('--display-theme'):
            s.display_theme = arg

    # Set serial
    if s.interface == 'i2c':
        serial = i2c(port=s.i2c_port, address=s.i2c_address)
        if s.display == 'sh1106':
            s.device = sh1106(serial, width=s.display_width, height=s.display_height, rotate=0)
        elif s.display == 'ssd1306':
            s.device = ssd1306(serial, width=s.display_width, height=s.display_height, rotate=0)
        elif s.display == 'ssd1327':
            s.device = ssd1327(serial, width=s.display_width, height=s.display_height, rotate=0, mode='RGB')
    else:
        serial = spi(device=0, port=0)
        if s.display == 'ssd1351':        
            s.device = ssd1351(serial, width=s.display_width, height=s.display_height, rotate=1, mode='RGB', bgr=True)
        elif s.display == 'st7735':
            s.device = st7735(serial, width=s.display_width, height=s.display_height, rotate=3, mode='RGB')


    d.display_init("Test")

if __name__ == '__main__':
    try:
        main(sys.argv[1:])
    except KeyboardInterrupt:
        pass
