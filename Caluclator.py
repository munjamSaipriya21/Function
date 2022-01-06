def my_function(num1,operator,num2):

    if operator=="addition":
        add=num1+num2
        return add
    if operator=="sub":
        sub=num1-num2
        # print(sub)
        return sub
    if operator=="multifiction":
        multi=num1*num2
        return multi
    if operator=="madulus":
        madul=num1%num2
        return madul
    if operator=="division":
        divi=num1/num2
        return divi
    if operator=="flor division":
        flor_div=num1//num2
        return flor_div
num1=int(input("enter the number:"))
operator=input("enter the operator:")
num2=int(input("enter the number:"))
print(my_function(num1,operator,num2))