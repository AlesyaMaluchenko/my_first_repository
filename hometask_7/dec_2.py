def print_dec(function):
    def wrapper(*args):
        print(function(*args))
        print(*args, sep='\t')
    return wrapper

@print_dec
def foo(a, b, c):
    print(a+b, b+c, sep='\t')

print(foo(3, 4, 5))