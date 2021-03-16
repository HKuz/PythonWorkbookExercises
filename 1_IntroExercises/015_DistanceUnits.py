#!/usr/bin/env python3

feet = float(input('Enter a distance in feet: '))

# Validate input
while feet < 0:
    print('Invalid input: distance must be positive!')
    feet = float(input('Enter a distance in feet: '))

inches = feet * 12
yards = feet / 3
miles = feet / 5280

print(f'You entered {feet:,.1f} feet.')
print(f'The equivalent distance in inches is: {inches:,.1f}')
print(f'The equivalent distance in yards is: {yards:,.1f}')
print(f'The equivalent distance in miles is: {miles:,.1f}')
