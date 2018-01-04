from time import time

def cancel(func):
    def func_wrapper():
        print('{} is canceled!'.format(func.__name__))
    return func_wrapper

def count_execution(func):
    func_count = {}
    def func_wrapper(*args, **kwargs):
        # it's seams like it not really safe
        name = func.__name__
        count = (func_count[name] if name in func_count else 0) + 1
        result = func(*args, **kwargs)
        func_count[name] = count
        print(count)
        return result
    return func_wrapper


def catch(func):
    def func_wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(str(e))
    return func_wrapper
