def my_fizz(num):
    i=1
    while i<num:
        if i%3==0:
            print("fizz")
        if i%5==0:
            print("buzz")
        if i%3==0 and i%5==0:
            print("fizzbuzz")
        i=i+1
user=int(input("enter the number:"))
my_fizz(user)
