#!/usr/bin/env python3

CENT_PER_INCH = 2.54

height_feet = int(input('Enter the "feet" part of your height: '))
height_inches = int(input('Enter the "inches" part of your height: '))

total_height_inches = height_feet * 12 + height_inches

total_cent = total_height_inches * CENT_PER_INCH

print(f"Your height of {height_feet}'{height_inches} "
      f"is {total_cent:,.1f} centimeters.")
