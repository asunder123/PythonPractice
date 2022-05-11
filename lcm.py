class LoggingContextManager:
    def __enter__(self):
        print('LoggingContextManager.__enter__()')
        return 'You are in a with-block'

    def __exit__(self, exc_type,exc_val,exc_tb):
        print('LoggingContentManager.__exit__({},{},{})'.format(exc_type,exc_val,exc_tb))
        return 
