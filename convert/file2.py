p = 'home/asunder/convert/convert.py'

try:
    process_file(f)
except OSError as e:
    print(f'Error: {e}')
