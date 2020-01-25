print ("Compresion de listas 3")
l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
m = ["a","b"]
n = [s * v for s in m
	for v in l
	if v > 0] 