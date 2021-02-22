#!/usr/bin/env python 3

# Weight is in grams
WIDGET_WEIGHT = 75
GIZMO_WEIGHT = 112

# Collect user input for widgets
num_widgets = float(input('Enter number of widgets ordered: '))

# Input verification for widgets
while (num_widgets != int(num_widgets) or num_widgets < 0):
    print('ERROR: The number of widgets must be a positive integer!')
    num_widgets = float(input('Enter number of widgets ordered: '))

# Collect user input for gizmos
num_gizmos = float(input('Enter number of gizmos ordered: '))

# Input verification for gizmos
while (num_gizmos != int(num_gizmos) or num_gizmos < 0):
    print('ERROR: The number of gizmos must be a positive integer!')
    num_gizmos = float(input('Enter number of gizmos ordered: '))

order_weight = num_widgets * WIDGET_WEIGHT + num_gizmos * GIZMO_WEIGHT

print(f'Total order weight: {order_weight:.0f} grams')
