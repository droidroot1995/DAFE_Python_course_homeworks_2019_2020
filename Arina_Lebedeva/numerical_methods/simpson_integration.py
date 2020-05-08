def fun(x):
       return x*x

def simpson_int(fun, a, b, n):
    if n%2 == 1:
        n += 1
    dx = 1.0 * (b - a) / n
    sum = (fun(a) + 4 * fun(a + dx) + fun(b))
    for i in range(1, n // 2):
        sum += 2 * fun(a + (2 * i) * dx) + 4 * fun(a + (2 * i + 1) * dx)

    return sum * dx / 3

x = fun(x)
print (simpson_int(fun, 1, 10, 100))
