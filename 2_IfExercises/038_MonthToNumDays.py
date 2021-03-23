#!/usr/bin/env python3

long_months = ['january', 'jan', 'march', 'mar', 'may', 'july', 'jul',
               'august', 'aug', 'october', 'oct', 'december', 'dec']

short_months = ['april', 'apr', 'june', 'jun', 'september', 'sep',
                'november', 'nov']

# Get user input
month = input('Enter a month: ').lower()
days = None

# Find number of days
if month in ['feb', 'february']:
    days = '28 or 29'
elif month in long_months:
    days = 31
elif month in short_months:
    days = 30

# Output the result
if days:
    print(f'{month.title()} has {days} days.')
else:
    print('You entered an invalid month!')
