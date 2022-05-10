import math
def mandel(real, imag):
    """ Log of number of interactions needed to determine whether a complex point is in Mandelbrot set 
         Args :
             real : real coordinate
             image: imaginary coordinate """
    x = 0
    y = 0
    for i in range(1,257):
        if x*x + y*y > 4.0:
            break
        xt = real +x*x - y*y
        y = imag+2.0*x*y
        x = xt
        return int(math.log(i)*256/math.log(256))-1

def mandelbrot(size_x,size_y):
    """Make a mandelbrot set image"""
    return [[mandel((3.5 * x /size_x) -2.5, (2.0 * y /size_y) -1.0) for x in range(size_x)] for y in range(size_y)]


