def lcm(x,y):
	if x>y:
		greter = x
	else:
		greter = y

	while(true):
		if((greter%x==0) and (greter%y==0)):
			lcm = greter
			break
		greter+=1	


		