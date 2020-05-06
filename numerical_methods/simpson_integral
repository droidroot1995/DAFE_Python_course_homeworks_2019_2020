#метод Симпсона
import math
def fn(x):
    return math.sin(x)+math.cos(x)
def simpson_integral(fn, a, b, n):
    if n%2 == 1:
        n += 1
    dx = 1.0 * (b - a) / n
    sum = (fn(a) + 4 * fn(a + dx) + fn(b))
    for i in range(1, n // 2):
        sum += 2 * fn(a + (2 * i) * dx) + 4 * fn(a + (2 * i + 1) * dx)

    return sum * dx / 3
print("simpson_integral = {}".format(simpson_integral(fn,0,math.pi/4,10000)))    
    
    
