def patron():
	n1,n2 = 0,1
	for i in range(0,21):
		print("[ " , i , "] -> [ " , n2, "]")
		if i % 2.0 != 0:
			n2+=1