def fibonacci(N):
    n1 = 1
    n2 = 1
    for i in range(N):
        yield n1
        n1, n2 = n2, n1 + n2