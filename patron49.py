def patron():
	n1,n2 = 0,1
	n3 = 1
	for i in range(0,21):
		print("[ " , i , "] -> [ " , n2, "]", "->[ ", n3 , " ]")
		if i % 2.0 != 0:
			n2+=1
		if n3 == 3:
			n3 = 0
		n3 +=1