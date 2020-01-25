def fibSuma():
	n1=0
	n2 =1
	suma =0
	print("Calculando....")
	for x in range(0, 99):
		total = n1  + n2
		if total > 99:
			break
		elif total <= 99:
			suma += total
			print("Sumando\t[ ",n1," + ", n2," ] = [ ",total, " ]  \t Acumulando -->[ ",suma, " ]")
			n1 = n2
			n2 = total
