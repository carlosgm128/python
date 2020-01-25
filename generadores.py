print("Los generadores son iguales que la compresion de listas \nPero estas devuelven un objeto no una lista\Ej.")

l1 = [1,2,3,4,5,6,7,8,9,10]
l2 = [n ** 2 for n in l1]
l3 = (n ** 2 for n in l1)

print("Las variables son:\nl1 la lista\nl2 la lista comprimida\nl3 el objeto generador")