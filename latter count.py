
def list_count(a):
    i=0
    count1=0
    while i<len(a):
        j=0
        while j<len(a[i]):
            if a[i][j]!=" ":
                count1+=1
            j+=1
        i+=1
    print(count1)
n=['my name is priya','I love chocolate']
list_count(n)





# a=['my name is priya','I love chocolate']
# i=0
# # b=[]
# count1=0
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         if a[i][j]!=" ":
#             count1+=1
#         j+=1
#     i+=1
# print(count1)