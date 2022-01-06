str=input("enter any string name:")
i=0
d=0
str1=""
while i<len(str):
    c=0
    j=0
    while j<len(str):
        if str[i]==str[j]:
            c+=1
        j+=1
    if str[i] not in str1:
        str1+=str[i]
        d=c
        print(str[i],d)
    i+=1