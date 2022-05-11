
def modulus_three(n):
 r = n % 3
 if r == 0:
     print("Multiple of three")
 elif r == 1:
     print("Remiander 1")
 else:
     assert r ==2 , "Remainder is not 2"
     print("Remainder 2")


def modulus_four(n):
    r = n % 4
    if r == 0:
        print("Multiple of 3")
    elif r == 1:
        print("Remainder 1")
    elif r == 2:
        assert r == 2, "Remainder is not 2"
        print("Remainder 2")
    elif r == 3:
        print("Remainder 4")
    else: 
        assert False, "This should'nt happen"
