#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
OledScroll 
'''

import settings as s
import lib as l
import time

from luma.core.render import canvas
from luma.core import legacy

from PIL import ImageFont

icon = ImageFont.truetype('./fonts/fontello.ttf', 14)     # Icon font
font = ImageFont.truetype('./fonts/7x5.ttf', 8)           # Text font
#font_big = ImageFont.truetype('./fonts/dot.ttf', 30)    # Text font
font_big = ImageFont.truetype('./fonts/bold.ttf', 30)    # Text font
font_tot = ImageFont.truetype('./fonts/rounded_led_board.ttf', 20)    # Text font

# Manage color
def get_color(section, value):
    color = s.theme.get(section, value)
    if color in s.color:
        return s.color[color]
    else:
        return color

# Print display on 128 x 64
def display_init(init_message):
    with canvas(s.device) as draw:
        draw.rectangle((0, 0, s.device.width - 1, s.device.height - 1), fill='black')

        position = 0
        for message in init_message:
            w, h = draw.textsize(text=message, font=font)
            tab = (s.device.width - w) / 2
            draw.text((tab, position), message, font=font, fill='white')
            position += 8
