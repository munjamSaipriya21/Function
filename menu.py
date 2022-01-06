def NG_menu(day,time):
    if day=="monday":
        if time=="breakfast":
            return "poha"
        elif time=="lunch":
            return "paneeer,rice,dal"
        elif time=="dinner":
            return "rajma,rice,chapathi"
        else:
            return "nothing"
    elif day=="tuesday":
        if time=="breakfast":
            return "dosa"
        elif time=="lunch":
            return "chapti,chole,rice,dal"
        elif time=="dinner":
            return "chicken,rice,chapathi"
        else:
            return "nothing"
n=input("enter the day:")
m=input("enter the time:")
print(NG_menu(n,m))

