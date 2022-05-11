import contextlib
import sys

@contextlib.contextmanager
def logging_context_manager():
    print('logging_context_manager: enter')
    try:
        yield 'You are in a with block'
        print('logging manager: normal exit',sys.exc_info())
    except Exception:
        print('logging_context_manager: exceptional exit',sys.exc_info())

