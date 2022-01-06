def max(m):
    i=0
    large=0
    while i<len(m):
        if num[i]>large:
            large=m[i]
        i=i+1
    print(large)
num=[3,5,7,34,2,89,2,5]
max(num)

def sum(add):
    i=0
    sum=0
    while i<len(add):
        sum=sum+add[i]
        i=i+1
    print(sum)
num=[1,2,3,4,5]
sum(num)

def sort(list1):
    list1.sort()
    print(unorder_list)
unorder_list = [6, 8, 4, 3, 9, 56, 0, 34, 7, 15]
sort(unorder_list)

def reverse(Reverse):
    Reverse .reverse()
    print( reverse_list)
reverse_list = ["Z", "A", "A", "B", "E", "M", "A", "R", "D"]
reverse(reverse_list )

def min(n):
    i=0
    list1.sort()
    print(n[i])
list1= [8, 6, 4, 8, 4, 50, 2, 7]
min(list1)
