# check frequency
n = int(input("enter number in which you want to check frequency here:"))
digit = int(input("enter number  here which you want to check frequency here:"))

count = 0

while n > 0:
    if n % 10 == digit:
        count += 1
    n //= 10

print(count)
