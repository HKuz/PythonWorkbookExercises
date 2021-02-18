#!/usr/bin/env python3

width = float(input('Enter the width of your field in feet: '))
length = float(input('Enter the length of your field in feed: '))

area_in_feet_sq = width * length

area_in_acres = area_in_feet_sq / 43560

print(f'The area of your field is {area_in_acres:.1f} acres.')
