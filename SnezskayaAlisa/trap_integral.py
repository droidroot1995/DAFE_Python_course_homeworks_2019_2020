#метод трапеций
import math
def fn(x):
    return math.sin(x)+math.cos(x)
def trap_integral(f,minx,maxx,n):
    dx=(maxx-minx)/n
    area=0
    x=minx
    for i in range(n):
        area+=dx*(f(x)+f(x+dx))/2
        x+=dx
    return area
print("trap_integral = {}".format(trap_integral(fn,0,math.pi/4,10000)))
 
