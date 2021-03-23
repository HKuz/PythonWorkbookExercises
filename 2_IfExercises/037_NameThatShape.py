#!/usr/bin/env python3

sides_to_shapes = {0: 'point',
                   1: 'line',
                   2: 'angle',
                   3: 'triangle',
                   4: 'rectangle or square',
                   5: 'pentagon',
                   6: 'hexagon',
                   7: 'heptagon',
                   8: 'octagon',
                   9: 'nonagon',
                   10: 'decagon',
                   11: 'hendecagon',
                   12: 'dodecagon'}

sides = int(input('Enter the number of sides for a shape from 0 to 12: '))

if sides in sides_to_shapes.keys():
    shape = sides_to_shapes[sides]
    modifier = 'a' if sides != 2 else 'an'
    print(f'A shape with {sides} sides is {modifier} {shape}.')
else:
    print('Sorry, you entered an invalid number of sides.')
