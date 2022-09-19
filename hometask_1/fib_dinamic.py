numb = int(input())
arr = [1, 1] + [0] * (numb - 1)
def fib_din(n):
    if arr[n - 1] != 0:
        return arr[n - 1]
    else:
        arr[n - 1] = fib_din(n - 1) + fib_din(n - 2)
    return arr[n - 1]

print(fib_din(numb))
