def list_change(a,b):
    i=0
    c=[]
    while i<len(a):
        m=(a[i]*b[i])
        c.append (m)
        i=i+1
    return c
print(list_change([5,10,50,20],[2,20,3,5]))
