import random
import math
import sympy
import numpy

x = sympy.symbols('x')


def bisection(a, b, f, e, maximum_iteration):
    iteration = 0
    temp_a = a
    temp_b = b
    while f(a) * f(b) > 0 and iteration < maximum_iteration:
        a = random.uniform(temp_a, temp_b)
        b = random.uniform(temp_a, temp_b)
        iteration += 1
    if iteration == maximum_iteration:
        print("Function does not meet initialization criterion.")
        return None
    iteration = 0
    while iteration < maximum_iteration:
        c = (a+b)/2
        iteration += 1
        if f(a) * f(c) < 0:
            b = c
        elif f(c) * f(b) < 0:
            a = c
        if abs(f(c)) < e:
            break
    print(iteration)
    return c


def newtons_method(function: sympy.Add, x0, error, max_iteration): # function is a sympy expresion.
    x1 = x0
    x2 = x0
    iteration = 0
    while iteration < max_iteration:
        iteration += 1
        x2 = x1 - (float(function.subs(x, x1))/float(sympy.diff(function, x).subs(x, x1)))
        x1 = x2
        if abs(float(function.subs(x, x2))) < error:
            break
    print(iteration)
    return x2


def test_1(x):
    return (x**4) - (12.3*(x**3)) + (6.8*(x**2)) + (185.1 * x) + 189


def test_2(x):
    return math.exp(x) + (x**2) + 100 - (6 * (x**3))


f1 = (x**4) - (12.3*(x**3)) + (6.8*(x**2)) + (185.1 * x) + 189
f2 = sympy.exp(x) + (x**2) + 100 - (6 * (x**3))

print(bisection(-3, 0, test_1, 0.0001, 1000))
print(bisection(-2, 6, test_2, 0.0001, 1000))
print(newtons_method(f1, -1, 0.0001, 1000))
print(newtons_method(f1, -2, 0.0001, 1000))
print(newtons_method(f2, 2, 0.0001, 1000))
