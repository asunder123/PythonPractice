def my_decorator(f):
  def wrap(*args,**kwargs):
      x = f(*args, **kwargs)
      return str(x).split()
  
  return wrap

@my_decorator
def func(x,y):
    return x+y
