def fibRange(ini,fin):
	n1,n2 = 0, 1
	total = 0
	i = 0
	for x in range(0,99):
		total = n1 + n2
		if total >= ini and total <= fin:
			i+=1
			print("[ ", total , " ]----> [ ", i ," ] Coincidencias")
			
		if total >= fin:
			break
		n1 = n2
		n2 = total
