# def my_function():
#     def sum (a,b):
#         return a+b
#     def sub (a,b):
#         return a-b
#     def multi (a,b):
#         return a*b
#     def division (a,b):
#         return a/b
#     print(sum(n,m))
#     print(sub(n,m))
#     print(multi(n,m))
#     print(division(n,m))
# n=int(input("enter the number:"))
# m=int(input("entyer number:"))
# my_function()

def sum (a,b):
    sum=a+b
    return sum
def sub (a,b):
    sub=a-b
    return sub
def multi (a,b):
    multi=a*b
    return multi
def division (a,b):
    division= a/b
    return division
def my_function():
    print(sum(n,m))
    print(sub(n,m))
    print(multi(n,m))
    print(division(n,m))
n=int(input("enter the number:"))
m=int(input("entyer number:"))
my_function(n,m)



