def revers_dec(function):
    def wrapped(*args):
        reverse = args[::-1]
        return function(*reverse)
    return wrapped

@revers_dec
def foo(a, b):
    return int(a)/int(b)

print(foo(3, 5))


