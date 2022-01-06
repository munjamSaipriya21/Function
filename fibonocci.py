def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = 10

if nterms <= 0:
   print("Plese enter a positive integer")
else:
    print("Fibonacci sequence:")
    i=0
    while i<10:
        print(recur_fibo(i))
        i=i+1


# def recur_fibo(n):
#    if n <= user:
#        return n
#    else:
#        return(recur_fibo(n-1) + recur_fibo(n-2))

# nterms = 10

# if nterms <= 0:
#    print("Plese enter a positive integer")
# else:
#     print("Fibonacci sequence:")
#     i=0
#     while i<10:
#         print(recur_fibo(i))
#         i=i+1
# user=int(input("enter the number:"))
# recur_fibo(user)
