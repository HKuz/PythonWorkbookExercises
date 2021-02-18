#!/usr/bin/env python3

SQUARE_FEET_PER_ACRE = 43560

width = float(input('Enter the width of your field in feet: '))
length = float(input('Enter the length of your field in feed: '))

area_in_feet_sq = width * length

area_in_acres = area_in_feet_sq / SQUARE_FEET_PER_ACRE

print(f'The area of your field is {area_in_acres:.1f} acres.')
