#метод прямоугольников
import math
def fn(x):
    return math.sin(x)+math.cos(x)
def rect_integral(f,minx,maxx,n):
    dx = (maxx-minx)/n
    area = 0
    x = minx
    for i in range(n):
        area += dx*f(x)
        x += dx
    return area
print("rect_integral = {}".format(rect_integral(fn,0,math.pi/4,10000)))    
    
