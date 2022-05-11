import contextlib

@contextlib.contextmanager
def nest_test(name):
    print('Entering', name)
    yield
    print('Exiting', name)
