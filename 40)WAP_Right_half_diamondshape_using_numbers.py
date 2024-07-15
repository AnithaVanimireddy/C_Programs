n=int(input())
num=1
#upper triangle
for i in range(0,n):
	for j in range(0,i+1):
		print(num,end=" ")
		num=num+1
	print()
#lower triangle
for i in range(n):
    for j in range(n - i - 1):
        print(num, end=" ")
        num=num+1
    print()
