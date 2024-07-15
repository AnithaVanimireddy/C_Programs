str1="Geeks for Geeks"
lower=0
upper=0
for i in str1:
	if (i.islower()):
		lower+=1
	else:
		upper+=1
print("lowercase letters is:",lower)
print("uppercase letters is:",upper)
