# def my_string(x,y):
#     if len(x)>len(y):
#         print(x)
#     else:
#         print(y)
#         print(x)
# n=input("enter the string:")
# m=input("enter the string:")
# my_string(n,m)


def my_string(x,y):
    i=0
    while i<len(x):
        if len(x)>len(y):
            print(x)
        else:
            print(y)
        i=i+1
#my_string("hello","welcome")
#my_string("sonu","manu")
n=input("enter the string:")
m=input("enter the string:")
my_string(n,m)


