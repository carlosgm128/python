def decorador(func):
	def nueva(*args):
		print ("Llamada a la funcion", func.__name__)
		retorno = func(*args)
		return retorno
	return nueva
def imp(s):
	print (s)
