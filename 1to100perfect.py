def my_perfect(a):
    per=1
    while per<a:
        i=1
        sum=0
        while i<per:
            if per%i==0:
                sum+=i
            i+=1
        if per==sum:
            print(per,"perfect number")
        per+=1
user=int(input("enter the number:"))
print(my_perfect(user))



#n=int(input("enter the number:"))
#per=1
#while per<n:
#   i=1
#    sum=0
#    while i<per:
#        if per%i==0:
#            sum+=i
#        i+=1
#    if per==sum:
#        print(per,"perfect number")
#    per+=1