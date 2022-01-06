def my_function(a): 
    i=0
    while i<=a:
        if i%2==0:
            print("even number",i)
        else:
            print("odd number",i)
        i=i+1
n=int(input("enter the numbrer:"))
my_function(n)