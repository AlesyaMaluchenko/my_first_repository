def hoar(arr, d=1, part='left'):
    if len(arr) > 1:
        bar = arr[0]
        left = []
        middle = []
        right = []
        for n in arr:
            if n < bar:
                left.append(n)
            elif n == bar:
                middle.append(n)
            else:
                right.append(n)

        hoar(left, d + 1)
        hoar(right, d + 1, part='right')
        k = 0
        for x in left + middle + right:
            arr[k] = x
            k += 1
    return (arr)

A = input().split()
print(*hoar(A))