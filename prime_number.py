def prime_number(n):
    i=1
    c=0
    while i<=n:
        if n%i==0:
            c=c+1
        i=i+1
    if c==2:
        print("prime")
    else:
        print("not a prime")
num=int(input("enter number:"))
print(prime_number(num))

n=int(input("enter the number:"))
i=1
while i<=n:
    j=1
    count=0
    while j<=i:
        if i%j==0:
            count+=1
        j=j+1
    if count==2:
        print(i,"prime")
    i=i+1

