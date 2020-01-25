
def fib(n):

	if n <=0:
		print("\\(-.-)/ OMG u are so dumb")
	else:
		print("Comprobando")
		n1 , n2 = 0, 1
		for x in range(0 , 99 ,1):
			total = n1 + n2
			print(total "<---checking")
			n1 = n2
			n2 = total
			if total == n:
				print("encontrado [", n, "]")
				break
			elif total >= 99:
				print("ninguna coincidencia encontrada")
				break
#			c+=1
		print("END")

