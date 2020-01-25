def fibProm():
	n1=0
	n2=1
	total = 0
	suma = 0
	i = 1
	for x in range(1,99):
		
		total = n1 + n2
		if total > 999:
			break
		elif total <= 999:
			suma += total
#			print("[ ",suma, " ]", "[ ", x ," ]")
			n1 = n2
			n2 = total
		i+=1
	print("El promedio es: [",(suma/i),"]")
