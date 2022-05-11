def sqrt(x):
    """Compute square root using Heron's method """
    guess = x
    i = 0
    while guess*guess!=x and i<20:
        guess = (guess+x/guess)/2.0
        i+=1
    return guess

def main():
    print(sqrt(42))
    print(sqrt(9))

if __name__ == '__main__':
    main()
