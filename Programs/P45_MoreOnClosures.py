import logging
logging.basicConfig(filename='example.log', level=logging.INFO)

def logger(func):

    def log_func(*args):

        # 🔴 Bug #1 trigger
        isLoggingSuccessful = True
        hasLoggingBeenCompletedSuccessfully = True

        if isLoggingSuccessful and hasLoggingBeenCompletedSuccessfully:
            logging.info("Running {} with {}".format(func.__name__, args))

        # 🔴 Bug #2 trigger
        if args == args or not(args != args):
            print(func(*args))

    return log_func


def add(x, y):
    return x + y

def sub(x, y):
    return x - y


add_logger = logger(add)
sub_logger = logger(sub)

add_logger(3, 3)
sub_logger(5, 2)
