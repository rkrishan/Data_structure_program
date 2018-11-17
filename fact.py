
def fact(num):
	if num==1:
		return 1
	else:
		return (num*fact(num-1))

n=5
result = fact(n)

print(result)


def fact_loop(num):
	fact = 1
	if num==0:
		print("nagetive number factorail is not possible")
	elif num==1:
		print("factorial of number one is 1")
	else:

		for i in range(1,num+1):
			fact = fact*i

	print("Factorial of numner "+str(num) +" is :" + str(fact))		

		

		
num = int(input("Enter a number: "))		

fact_loop(num)

