#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
OledScroll 
'''

# Version

version = '0.0.1'

# Default i2c_port, i2c_address, display and room

interface = 'i2c'                       # Default value !
i2c_port = 0                            # Default value ! Check with i2detect
i2c_address = 0x3C                      # Default value ! Check with i2detect
display = 'ssd1327'                     # Default value !
display_width = 128                     # Default value !
display_height = 128                    # Default value !
display_theme = 'gray.cfg'              # Default value ! 
follow = 'RRF'                          # Default value !
refresh = 1.0                           # Default value !
latitude = 48.8482855                   # Default value ! Check WGS84 on https://www.coordonnees-gps.fr/
longitude = 2.2708201                   # Default value ! Check WGS84 on https://www.coordonnees-gps.fr/
