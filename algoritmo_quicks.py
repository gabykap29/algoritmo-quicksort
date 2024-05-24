import random

#crear una lista de numeros random
lista_numeros = []
for i in range(0,10):
    lista_numeros.append(random.randint(0, 10))
    

#ordenar la lista con quicksort

def quicksort(array):
    # si la lista tiene un elemento o no se retorna la lista
    if len(array) < 2:
        return array
    # si la lista tiene dos elementos se vuelve a llamar a la funcion
    else:
        #primer elemento como pivote
        pivote = array[0]
        #menores que el pivote
        menores = [x for x in array[1:] if x <= pivote] #el metodoo [1:] es para saltar el pivote, ya que el pivote ya esta en la lista
        #mayores que el pivote
        mayores = [x for x in array[1:] if x > pivote] #el metodoo [1:] es para saltar el pivote, ya que el pivote ya esta en la lista
        #retornar la lista ordenada con los menores y el pivote y los mayores
        return quicksort(menores) + [pivote] + quicksort(mayores)
    
#ejecutar el algoritmo
print(quicksort(lista_numeros))