def factorial(n):
    fact=1
    while n>0:
        fact=fact*n
        n=n-1
    print(fact,"factorial")
user=int(input("enter the number:"))
factorial(user)