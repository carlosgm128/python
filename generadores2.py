print("Generador 2")
print("Un generador es una calse especian de funcion por la que nos permite generar valores los que podemos iterar")
print("Ejemplo")

def generador(n,m,s):
	while(n <= m):
		yield n
		n += s
print("Si llamas la funcion Generador con 3 parapetros")