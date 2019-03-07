

def fib():
    fibnums = []
    evensums = []
    x = 1
    y = 2
    fibnums.append(x)
    fibnums.append(y)
    while fibnums[-1] < 4000000:
        f = fibnums[-1] + fibnums[-2]
        fibnums.append(f)
    for x in fibnums:
        if x % 2 == 0:
            evensums.append(x)
    print(evensums)
    print(sum(evensums))





    print(fibnums)
fib()
