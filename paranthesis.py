n=input("enter the paranthesis:")
i=0
count_open=0
count_close=0
while i<len(n):
    if n[i]=="(":
        count_open+=1
    elif n[i]==")":
        count_close+=1
    i=i+1
if count_open==count_close:
    print("valid")
else:
    print("not valid")


n=input("enter the paranthesis:")
if len(n)%2==0:
    print("valid")
else:
    print("not valid")

  


# n=input("enter the paranthesis:")
# if n=="()":
#     print("valid")
# else:
#     print("not valid")


