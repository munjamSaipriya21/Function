def max_list(n):
	i=0
	max=0
	while i<len(n):
		j=0
		while j<len(n[i]):
			if n[i][j]>max:
				max=n[i][j]
			j=j+1
		i=i+1
		print(max)
num_list= [[45, 21, 42, 63], [12, 42, 42, 83], [42, 90, 78, 13], [94, 89, 78, 76], [87, 55, 98, 99]]       
max_list(num_list)





# n= [[45, 21, 42, 63], [12, 42, 42, 53], [42, 90, 78, 13], [94, 89, 78, 76], [87, 55, 98, 99]]
# i=0
# max=0
# while i<len(n):
# 	    j=0
# 	    while j<len(n[i]):
# 	        if max<n[i][j]:
# 	        	max=n[i][j]
# 	        j=j+1
# 	    i+=1
# 	    print(max)
