#!/usr/bin/env python3

"""
US: Miles / Gallon
CAN: Liters / 100 kilometers
"""

KM_PER_MILE = 1.609
L_PER_GAL = 3.785

mpg = float(input('Enter Miles per Gallon (MPG) efficiency: '))

# Convert miles/gallon to km/gallon
km_per_gal = mpg * KM_PER_MILE

# Invert to get gallons/km
gal_per_km = 1 / km_per_gal

# Convert gallons/km to liters/km
l_per_km = gal_per_km * L_PER_GAL

# Divide by 100 to get liters/100km
l_per_100km = l_per_km * 100

print(f'{mpg:.0f} MPG is equivalent to {l_per_100km:.2f} liters/100km.')
