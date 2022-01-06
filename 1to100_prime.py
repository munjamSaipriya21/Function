def prime_number(n):
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
user=int(input("enter the number:"))
prime_number(user)



