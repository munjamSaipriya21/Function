def my_function(num):
    i=1
    while i<num:
        if i%3==0:
            print(i,"nav")
        if i%7==0:
            print(i,"gurukul")
        if i%21==0:
            print(i,"navgurukul")
        i=i+1
user =int(input("enter the number:"))
my_function(user)