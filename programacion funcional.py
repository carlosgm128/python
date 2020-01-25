def saludar(lang): #declaramos la funcion con un argumento
	def saludar_es(): #funcion en ES
		print("Hola")
	def saludar_en(): #funcion en EN
		print("Hello")
	def saludar_fr(): #Funcion en FR
		print("Salut")
	#Declaramos una funcion con un diccionario para que cuando el usuario cree un objeto con el argumento sepa que funcion llamar
	# con el parametro llama a el parametro y el diccionario devuelve la funcion especificada en el
	# Fin 
	lang_func = {"es": saludar_es,
		"en": saludar_en,
		"fr": saludar_fr}
	return lang_func[lang]