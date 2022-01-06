def max_function():
    numbers_list1 = [1, 2, 3, 4, 5, 6,9, 7, 10, -2]
    i=0
    max=0
    while i<len(numbers_list1):
        if numbers_list1[i]>max:
            max=numbers_list1[i]
        i=i+1
    print (max)
max_function()

def max_function():
	numbers_list = [1, 2, 3, 4, 5, 6, 7, 10, -2]
	print (max(numbers_list))
max_function()


def my_len ():
    a=[1,2,3,4,5,6]
    print(len(a))
my_len()