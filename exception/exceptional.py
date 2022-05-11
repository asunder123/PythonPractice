import sys
from math import log

DIGIT_MAP={
        'zero' : '0',
        'one' :'1',
        'two' : '2',
        'three' : '3',
        'four' : '4',
        }

def string_log(s):
    v = convert(s)
    return log(v)

def convert(s):
    try:
       number=''
       for token in s:
           number +=DIGIT_MAP[token]
       return int(number)
    except (KeyError,TypeError) as e:
        print(f"Conversion error: {e!r}", file=sys.stderr)
    return -1
