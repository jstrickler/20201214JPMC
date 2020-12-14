from datetime import datetime
from functools import wraps

def time_stamp(old_function):  # old_function is the function being decorated

    @wraps(old_function)
    def _new():   # replacement function
        print(datetime.now().ctime())
        result = old_function()
        return result

    return _new

@time_stamp
def ham():
    return "Hello from ham()"
# ham = time_stamp(ham)

print(ham())

@time_stamp
def eggs():
    return "Hello from eggs()"

print(eggs())

print(ham.__name__, eggs.__name__)

routes = {}

def app(path):  # outer decorator

    def inner_decorator(old_function):
        routes[path] = old_function

        @wraps(old_function)
        def replacement():
            result = old_function()
            return result
        return replacement

    return inner_decorator


@app('/')
def foo():
    pass

# foo = app('/')(foo)

@app('/wombats')
def bar():
    pass

print(routes)
