def err_dec(function):
    def wrapped(*args):
        try:
            function(*args)
        except Exception:
            return "error..."
    return wrapped
@err_dec
def foo(a):
    return 3 + a
print(foo('dnfdf'))


