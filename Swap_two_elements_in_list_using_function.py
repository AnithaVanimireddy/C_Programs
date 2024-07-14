list1=[1,2,3,4,5]
def swaplist(list1,pos1,pos2):
	n=len(list1)
	temp=list1[pos1]
	list1[pos1]=list1[pos2]
	list1[pos2]=temp
	return list1
print(list1)
pos1=2
pos2=4
print(swaplist(list1,pos1,pos2))
