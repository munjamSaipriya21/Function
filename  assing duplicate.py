def my_list():
    a=[1,5,2,10,11,13,5]
    b=[5,10,20,16,17,3,3]
    i=0
    c=[]
    while i<len(a):
        if a[i] not in c:
            c.append (a[i])
            c.append (b[i])
            c.sort()
        i=i+1
    print(c)
my_list()




