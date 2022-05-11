def lookups():
    s = [1,4,5]
    try:
        items = s[6]
    except LookupError:
        print("Handled IndexError")
    d = dict(a=65, b=66, c=67)
    try:
        value = d['x']
    except LookupError:
        print("Handled KeyError")

if __name__ == '__main__':
    lookups()
