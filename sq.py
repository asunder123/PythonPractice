def raise_to(exp):
    def raise_to(x):
        return pow(x,exp)
    return raise_to
