## Первые шаги

print('ку-ку')

h = 0
while h< 10:
    h +=1

x = 2
x

x + 12

x = 11
y = 22
x + y

def fib(n):
    if n <= 1:
        return 1 
    else:
        return fib(n - 1) + fib(n - 2)

fib(12)

li = []
for i in range(1,10):
    li.append(i)
li

fibs = [(n, fib(n)) for n in range(1,10)]
fibs




## Квадратные уравнения



from math import sqrt

def solve(a, b, c):
    d = b**2 - 4*a*c
    if d >= 0:
        x1 = (-b + sqrt(d)) / (2 * a)
        x2 = (-b - sqrt(d)) / (2 * a)
        return (x1, x2)
    else:
        return 'Вещественных корней нет'


solve(0.5, 0.125, 0)    # (0.0, -0.25)



solve(1, 2, 3)


z1 = complex(1, 2)
z2 = complex(3, 5)
z1, z2
# (z1, z2)

'z1 = ({}, {})'.format(z1.imag, z2.real)


import cmath

def csolve(a, b, c):
    d = b**2 - 4*a*c
    x1 = (-b + cmath.sqrt(d)) / (2 * a)
    x2 = (-b - cmath.sqrt(d)) / (2 * a)
    return (x1, x2)

csolve(1, 2, 5)    # ((-1+2j), (-1-2j))





## Пример использования Map 




f = lambda x: x**3
list(map(f, range(1, 5)))








##  [PIP](https://pypi.org/)






import matplotlib.pyplot as plt
import random

random.randint(1, 10)


f = lambda x: random.randint(1, 10)
points = list(map(f, range(1, 10)))
points


p = plt.plot(points, 'b.') 


plt.plot(points)
plt.show()


x = list(map(f, range(1, 10)))
y = list(map(f, range(1, 10)))
print(x)
print(y)
# ., , , o, v, ^, <	, >, 1, 2, 3, 4, 8, s, p, P, *, h, H, +, x, X, D, d, |, _, 
plt.plot(x, y, 'rD')
plt.show()


x = list(range(1,200))
fx = [i*i for i in x]

# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.html?highlight=pyplot#
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axes.html#matplotlib.pyplot.axes

plt.axes(facecolor='white')
plt.plot(x,fx)
plt.show()






### Настройки
# https://matplotlib.org/stable/tutorials/introductory/customizing.html




import matplotlib.pyplot as plt
import matplotlib as mpl

x = list(range(-200, 200))
fx = [i**2 + 2*i - 3 for i in x]

# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.html?highlight=pyplot#
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axes.html#matplotlib.pyplot.axes

mpl.rcParams['lines.linewidth'] = 2
mpl.rcParams['lines.linestyle'] = '-.' #'--'
mpl.rcParams['lines.color'] = 'C0'

plt.axes(facecolor='white')
plt.plot(x,fx)
plt.show()



import matplotlib.pyplot as plt
plt.plot([1,2],[1,-1], 'ro', markerfacecolor = 'red')
plt.show()



import numpy as np
from math import sqrt
import matplotlib.pyplot as plt

x = list(range(0, 500, 2))
y = list(map(lambda a: sqrt(a),x))

fig, ax = plt.subplots()

ax.plot(x, y)
ax.grid()

#  Наименование осей
ax.set_xlabel('x')
ax.set_ylabel('sqrt(x)')
  
plt.show()



import matplotlib.pyplot as plt
import random

# random.randint(1, 10)

vx = [1.0,2.0,3.0]
vy = [1.0,2.0,1.0]

sx = vx[0]
sy = vy[0]

px = []
py = []

for i in range(1,1000):
    r = random.randint(0, 2)
    sx = (sx + vx[r]) / 2
    sy = (sy + vy[r]) / 2    
    px.append(sx)
    py.append(sy)
  
plt.plot(px, py, 'o')
plt.show()




import random
import matplotlib.pyplot as plt

x = [1.0,2.0,3.0]
y = [1.0,2.0,1.0]

sx = x[0]
sy = y[0]

px = []
py = []

for i in range(1,100000):
    r = random.randint(0, 2)
    sx = (sx + x[r]) / 2
    sy = (sy + y[r]) / 2    
    px.append(sx)
    py.append(sy)

fig, ax = plt.subplots()

# маркеры цветов 'b', 'g', 'r', 'c', 'm', 'y', 'k', 'w' , RGB: #00ff00
ax.scatter(px, py, c = 'red', s = 1)
ax.set_facecolor('black')

# ax.grid()
# ax.set_xlabel('')
# ax.set_ylabel('')
fig.set_figwidth(15)
fig.set_figheight(10)
plt.show()



### Кубик


import random
import matplotlib.pyplot as plt

count = 10000
x = list(range(1, 7))
y = [0 for i in x]

fig, ax = plt.subplots()

for _ in range(count):
    y[random.randint(0, 5)] += 1

ax.bar(x, y)
# 
y.sort()
#print('{}%'.format(round((y[5] - y[0]) / count * 100, 3)))
stat = [f'{i+1}: {round(y[i] / count * 100)}%' for i in range(0,6)]
print(stat)
plt.show()



from sympy import *
from sympy.plotting import plot
init_printing()


x = Symbol('x')


f = x + 2022
f


f.subs(x, -77)


f.subs(x,-210)


plot(f)
print(f)


g = sin(x+x)/x
plot(g)
print(g)


h = x**2
h


plot(h)
h

h=-h

plot(h)
h

a = 1
b = 0
c = 0
h = a*x**2 + b*x+c
h

plot(h)
h


a = 1
b = 3
c = 4
h = a*x**2 + b*x+c
h

plot(h)
h

solve(h, x)

q = x/(x+2)
q

plot(q)


fun1 = plot(q,(x,-10,-2.1), show=False)
fun2 = plot(q,(x,-1.9,10), show=False)
fun1.append(fun2[0])
fun1.show()


x = Symbol('x')
y = 1*x**2 + 2*x - 10
solve(y)

res = plot(y,(x,-5, 5))
