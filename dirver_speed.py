def driver_speed(speed):
    if speed<70:
        print("ok")
    else:
        a=[0,70,80,90,100,110,120,130,140,150,160,170,180]
        i=0
        while i<len(a):
            if a[i]>=speed:
                print(i,"point")
                break
            if i>=12:
                print("driver ko 12 points se jyaada License suspended")
            i=i+1
user=int(input("enter the number:"))
driver_speed(user)

            





