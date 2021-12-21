import math
from random import randrange

CommonOperations = ["+", "-", "*", "/"]
rad = math.pi/180

class Scientific_calc:
    def scientific_calc(user_input):
        d = user_input.split()
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
        
        def sum(a, b):
            if a > b:
                return 0
            else:
                return b + sum(a, b - 1)

                
        if "sqrt" in user_input:
            a = user_input.split("(")
            b = a[1]
            c = b.split(")")
            n = float(c[0])
            
            return sqrt(n)

        elif "!" in user_input:
            a = user_input.split("!")
            b = int(a[0])
            c = factorial(b)
            
            return c

        elif CommonOperations[0] in user_input:
            return int(d[0]) + int(d[2])

        elif CommonOperations[1] in user_input:
            return int(d[0]) - int(d[2])

        elif CommonOperations[2] in user_input:
            return int(d[0]) * int(d[2])

        elif CommonOperations[3] in user_input:
            return int(d[0]) / int(d[2])

        elif "sin" in user_input:
            a = user_input.split("(")
            b = a[1]
            c = b.split(")")
            n = float(c[0])
            return math.sin(rad*n)

        elif "cos" in user_input:
            a = user_input.split("(")
            b = a[1]
            c = b.split(")")
            n = float(c[0])
            return math.cos(rad*n)

        elif "tan" in user_input:
            a = user_input.split("(")
            b = a[1]
            c = b.split(")")
            n = float(c[0])
            return math.tan(rad*n)
        
        elif "sum" in user_input:
            a = int(d[2])
            b = int(d[4])
            c = sum(a, b)
            return c

    

