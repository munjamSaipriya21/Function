def strong_number(s):
    n=1
    while n<=s:
        m=n
        sum=0
        while m>0:
            i=1
            fact=1
            rem=m%10
            while i<=rem:
                fact=fact*i
                i=i+1
            sum=sum+fact
            m=m//10
        if sum==n:
            print(n,"strong number")
        n=n+1
us=int(input("enter the number:"))
strong_number(us)