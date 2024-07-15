def Perfect_num(n):
	rem=0
	for i in range(1,n):
		if (n%i==0):
			rem+=1
	if rem==n:
		print(n,"is perfect number")
	else:
		print(n,"is not perfect number")
	return " "
print(Perfect_num(32))
