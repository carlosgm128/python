def fact(n):
	fact = 1
	for i in range(1,n+1):
		fact = fact * i
	print("El factorial de ",n ,"= ", fact)