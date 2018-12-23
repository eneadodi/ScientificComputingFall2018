#!/usr/bin/env python3


a = int(input("amount:"))
<<<<<<< HEAD

def fib(n):
=======
def fib_gen(n):
>>>>>>> e61dd266bb651839fa336db86e56b63900578ddc
    a = 0
    b = 1
    for _ in range(n):
        yield a
        a = b
        b = a + b

<<<<<<< HEAD
print(list(fib(a)))
=======
print(list(fib_gen(a)))
>>>>>>> e61dd266bb651839fa336db86e56b63900578ddc
