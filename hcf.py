def find_hcf(x,y):
	if x>y:
		smaller = x
	else:
		smaller = y

	for i in range(1,smaller+1):
		if((x%i==0) and (y%i==0)):
			hcf = i
	return hcf	

x  = int(input("Enter a number x: "))		
y  = int(input("Enter a number y: "))		

	
result = find_hcf(x,y)

print("HCF of "+str(x) + " and "+str(y)+" is : " +str(result))		
		
		