def fact(n):
	total = n
	fact = 1
	prom = 0
	i = 0
	for f in range(1,total+1):
		fact = fact * f
		#print("fact--->",fact)
		prom = prom + fact
		#print("prom---->", prom)
		total-=1
		#i+=1
#		print("Promedio factorial de [ ",f," ]-->",(prom/f))
		print("Promedio total-->",(prom/n))
