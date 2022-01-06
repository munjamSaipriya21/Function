def distance(kms):
    if kms <20:
        print("close")
    elif kms <50:
        print("median")
    else:
        print("far")
n=int(input("enter the number:"))
distance(n)