def multi_sum(num):
    i=1
    sum=0
    while i<=num:
        if i%3==0 or i%5==0:
            print(i)
            sum=sum+i
        i=i+1
    print("sum=",sum)
user=int(input("enter the number"))
multi_sum(user)

# n=int(input("enter the number"))
# i=1
# sum=0
# while i<=n:
#    if i%3==0 or i%5==0:
#        print(i)
#        sum=sum+i
#    i=i+1
# print("sum=",sum)