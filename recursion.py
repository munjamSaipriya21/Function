# def add(n1,n2): #recursion like a loop it will repated
#     return add(n1,n2)
# print(add(2,3))

# def one_to_ten (number):
#     if number==1:
#         return 1
#     return one_to_ten(number-1)
# print(one_to_ten(10))


def one_to_ten(number):
    if number==1:
        print(1)
    return one_to_ten(number-1)
print(one_to_ten(5))

# def one_to_ten(number):
#     if number==1:
#         # print(1)
#         return 1
#     else:
#         return 1
# print(one_to_ten(5))