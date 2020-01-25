def factRange(n):
	total =n
	for i in range(1,n+1):
		fact = 1
		for f in range(1,total+1):
			fact = fact * f

		print("Factorial del numero [",total," ] = ",fact)
		total -=1

