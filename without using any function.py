# list1=[5,3,7,9,6,53,61,75,67]
# c=0
# for i in list1:
#     c+=1
# print(c)

# list1=[5,3,7,9,6,53,61,75]
# n=int(input("enter the number:"))
# count=0
# i=0
# # a=[]
# while i<=(n):
#     # a.append (n[i])
#     count+=1
#     i=i+1
# print(count)
    




def list_length(list1):
    sum=0
    if not list1:
        print("The list is empty.")

    if type(list1) == type([]):
        for item in (list1):
            sum+=1
        print("The length of the list is ",sum)

    else:
        print("The input is not a list.")


my_list = [1,12,15,100]
list_length(my_list)

# a=[2,32,7,9,87,5]
# c=0
# i=0
# while i not in a:
#     if type(a)==type([]):
#         c+=1
#     i=i+1
#     print(c)


