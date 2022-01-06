def my_function(num1,num2,operator):
    if operator=="+":
        sum=num1+num2
        return sum
    if operator=="*":
        multi=num1*num2
        return multi
    # else:
    #     divi=num1/num2
    #     return divi
n1=int(input("enter the number:"))
n2=int(input("enter the number:"))
operator=input("enter the operator:")
print(my_function(n1,n2,operator))
def list_change(a,b):
    i=0
    c=[]
    while i<len(a):
        m=my_function(a[i],b[i],"*")
        c.append (m)
        i=i+1
    return c
print(list_change([5,10,50,20],[2,20,3,5]))
