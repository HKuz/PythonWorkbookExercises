#!/usr/bin/env python3

# Conversion rate for first two dog years
YOUNG_DOG_CONV = 10.5

# Conversion rate for any year after first two
MATURE_DOG_CONV = 4

human = float(input('Enter your age in years: '))

while human < 0:
    human = float(input('Invalid input. Enter your age in years: '))

if human <= 2:
    dog = human * YOUNG_DOG_CONV
else:
    dog = 2 * YOUNG_DOG_CONV + (human - 2) * MATURE_DOG_CONV

print(f'Your age in dog years is: {dog}')
