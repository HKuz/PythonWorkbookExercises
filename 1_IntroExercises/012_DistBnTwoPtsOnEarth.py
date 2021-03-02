#!/usr/bin/env python3

"""
User enters latitude and longitude for two points on Earth's surface, the
program prints the distance in kilometers between them.

Point 1: (t1, g1)
Point 2: (t2, g2)

d = 6371.01 * arccos(sin(t1) * sin(t2) + cos(t1) * cos(t2) * cos(g1 - g2))
"""

import math


AVG_EARTH_RADIUS = 6371.01

lat_1 = math.radians(float(input('Degrees latitude of pt 1: ')))
lon_1 = math.radians(float(input('Degrees longitude of pt 1: ')))
lat_2 = math.radians(float(input('Degrees latitude of pt 2: ')))
lon_2 = math.radians(float(input('Degrees longitude of pt 2: ')))

sin_lats = math.sin(lat_1) * math.sin(lat_2)
cos_lats = math.cos(lat_1) * math.cos(lat_2) * math.cos(lon_1 - lon_2)

distance = AVG_EARTH_RADIUS * math.acos(sin_lats + cos_lats)

print(f'The distance between your points is {distance:,.1f}km')
