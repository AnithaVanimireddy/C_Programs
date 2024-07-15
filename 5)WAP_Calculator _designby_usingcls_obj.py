class Calculator:
	def add(self,x,y):
		return x+y
	def subtract(self,x,y):
		return x-y
	def multiply(self,x,y):
		return x*y
	def divide(self,x,y):
		if y!=0:
			return x/y
		else:
			return ("can not divide by zero")
calculator=Calculator()
result=calculator.add(5,3)
print(result)
result=calculator.subtract(5,3)
print(result)
result=calculator.multiply(5,3)
print(result)
result=calculator.divide(10,2)
print(result)
