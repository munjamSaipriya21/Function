def harsad_number(m):
    n=1
    while n<=m:
        r=n
        sum=0
        while r>0:
            rem=r%10
            sum=sum+rem
            r=r//10
        if n%sum==0:
            print(n,"harsad number")
        n=n+1
user=int(input("enter the number:"))
harsad_number(user)