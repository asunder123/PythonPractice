import os 
import sys

p = '/home/asunder/convert/convert.py'

try:
    if os.path.exists(p):
       process_file(p)
    else:
        print(f'No such file as {p}')

except OSError as e:
    print(f'Error: {e}')


