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





def scientific_calc():
    CommonOperations = ["+", "-", "*", "/"]
    rad = math.pi/180
    msg = input("")
    d = msg.split()

    if "sqrt" in msg:
        a = msg.split("(")
        b = a[1]
        c = b.split(")")
        n = float(c[0])
        print(sqrt(n))
    elif "!" in msg:
        a = msg.split("!")
        b = int(a[0])
        c = factorial(b)
        print(c)
    elif CommonOperations[0] in msg:
        print(int(d[0]) + int(d[2]))
    elif CommonOperations[1] in msg:
        print(int(d[0]) - int(d[2]))
    elif CommonOperations[2] in msg:
        print(int(d[0]) * int(d[2]))
    elif CommonOperations[3] in msg:
        print(int(d[0]) / int(d[2]))
    elif "sin" in msg:
        a = msg.split("(")
        b = a[1]
        c = b.split(")")
        n = float(c[0])
        print(math.sin(rad*n))
    elif "cos" in msg:
        a = msg.split("(")
        b = a[1]
        c = b.split(")")
        n = float(c[0])
        print(math.cos(rad*n))
    elif "tan" in msg:
        a = msg.split("(")
        b = a[1]
        c = b.split(")")
        n = float(c[0])
        print(math.tan(rad*n))
 # todo add the inverse trigonometric functions here
    else:
        await.channel.send(random.choice(doge_gifs))


scientific_calc()
