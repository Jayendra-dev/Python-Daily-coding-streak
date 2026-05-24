# using functions find factorial of a number.
n=int(input("enter n:"))
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

print(factorial(n))
