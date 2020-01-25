def fib(nter):
	if nter <= 1:
		print("\(-.-)/ U ARE SO DUMB")
		
	else:
		n1,n2 = 0,1
		count = 0
		while count < nter:
			print("STEP:",count, " = [ " , n1, " ]")
			total = n1 + n2
			n1 = n2
			n2 = total
			count +=1
	print("END")
