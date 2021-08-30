import math
from random import randrange


def sqrt(n):
    a = randrange(10)
    for i in range(500):
        a = (n + a ** 2) / (2 * a)
    return a


def factorial(n: int) -> int:
    if n == 0:
        return 1
    elif n > 0:
        return n * factorial(n - 1)


CommonOperations = ["+", "-", "*", "/"]
rad = math.pi/180


def scientific_calc():
    user_input = input("")
    d = user_input.split()

    if "sqrt" in user_input:
        a = user_input.split("(")
        b = a[1]
        c = b.split(")")
        n = float(c[0])
        print(sqrt(n))
        scientific_calc()
    elif "!" in user_input:
        a = user_input.split("!")
        b = int(a[0])
        c = factorial(b)
        print(c)
        scientific_calc()
    elif CommonOperations[0] in user_input:
        print(int(d[0]) + int(d[2]))
        scientific_calc()
    elif CommonOperations[1] in user_input:
        print(int(d[0]) - int(d[2]))
        scientific_calc()
    elif CommonOperations[2] in user_input:
        print(int(d[0]) * int(d[2]))
        scientific_calc()
    elif CommonOperations[3] in user_input:
        print(int(d[0]) / int(d[2]))
        scientific_calc()
    elif "sin" in user_input:
        a = user_input.split("(")
        b = a[1]
        c = b.split(")")
        n = float(c[0])
        print(math.sin(rad*n))
        scientific_calc()
    elif "cos" in user_input:
        a = user_input.split("(")
        b = a[1]
        c = b.split(")")
        n = float(c[0])
        print(math.cos(rad*n))
        scientific_calc()
    elif "tan" in user_input:
        a = user_input.split("(")
        b = a[1]
        c = b.split(")")
        n = float(c[0])
        print(math.tan(rad*n))
        scientific_calc() # todo add the inverse trigonometric functions here
    elif "off" in user_input:
        exit(0)
    else:
        scientific_calc()


scientific_calc()
