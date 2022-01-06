def duplicates(name):
    i=0
    a=[]
    while i<len(name):
        if name[i] not in a:
            a.append(name[i])
        i=i+1
    print(a)
string_list = ["Rishabh", "Rishabh", "Abhishek", "Rishabh", "Divyashish", "Divyashish"]
duplicates(string_list)

def assigneding(n):
    i=0
    a=[]
    while i<len(n):
        n=list2+list1
        n.sort()
        # print(n)
        if n[i] not in a:
            a.append(n[i])
        i=i+1
    print(a)
list1 = [1, 342, 75, 23, 98]
list2 = [75, 23, 98, 12, 78, 10, 1]
assigneding(list2)