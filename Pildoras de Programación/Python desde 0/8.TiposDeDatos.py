import time

time.sleep(1)

# ENTEROS-----------------------------------------------------------------
print("---INT---")
# Los enteros no tienen un límite, el unico límite es el espacio de memoria del computador
entero = 1233333333333333333333333333333333333333333123213
# Podemos dividir entre enteros
int1 = 10
int2 = 4
print(int1 / int2)
print(int1 // int2)
print(int1 % int2)

# BOOLEANOS-----------------------------------------------------------------
print("---BOOL---")
var1 = True
var2 = False
print(int(var1) + True)

# FLOAT-----------------------------------------------------------------
print("---FLOAT---")
print(0.6 + 0.7)  # Retorna 1.2999999999999998, para retornar el valor exacto se debe trabajar con decimal

# STRING-----------------------------------------------------------------
print("---STRING---")
nombre1 = "Steven"
nombre2 = 'Edward'
texto = ''' Hola
Este es un texto de prueba que permite
saltar de linea por su formato
'''
print(texto)
print(len(nombre1))

# Se puede eliminar sufijos y prefijos
producto1 = "0001 - Manzana"
producto2 = "Manzana - 0001"
print(producto1.removeprefix('0001 - '))
print(producto2.removesuffix(' - 0001'))

# Indexing: Se accede a un caracter de un string
string1 = "12345"
print(string1[0])  # Acceder al elemento 0 de string1
print(string1[-1])  # Acceder al ultimo elemento
print(string1[-2])  # Acceder al pen-ultimo elemento

# Slicing: Divide un string
cadena = "Hola, Mundo!"
print(cadena[0:4])
print(cadena[6:])
print(cadena[::2])  # Se accede a los caracteres de saltos de 2 en 2 desde inicio a fin
print(cadena[-6:-1])  # Slicing Negativo
print(cadena[::-1])

cellphone = "1-2-3-4-5-6"
print(cellphone[::2])
cellphone = "-1-2-3-4-5-6"
print(cellphone[1::2])

# MUTABILIDAD E INMUTABILIDAD-----------------------------------------------------------------
# Datos mutables permiten ser cambiados después de que fueron definidos (listas, sets, diccionarios)
# Datos inmutables no permiten ser cambiados después de que fueron definidos

# Este es un problema de objetos mutables
lista1 = ["1", "2", "3"]
lista2 = lista1
lista2.append("4")
print(
    f'Lista 1: {lista1} y Lista 2: {lista2}')  # lista1 es modificada desde la variable lista2 por el concepto de mutabilidad

# TUPLES -----------------------------------------------------------------
# Es un lista inmutable que permite almacenar una secuencia de objetos
mi_tuple = (1, False, 'Edward', 0.145)


def retornar_estudiante():
    return 'Edward', 28, 8.6


tupla1 = retornar_estudiante()
print(tupla1)

nombre, edad, promedio = retornar_estudiante()
print(f'Nombre: {nombre}, Edad: {edad}, Promedio: {promedio}')

# ONE-LINE SWAPPING
variable1 = 1.0
variable2 = 2.0

variable1, variable2 = variable2, variable1

# LISTAS-----------------------------------------------------------------
lista1 = [1, 2, 2, 3, 3, 3, 4]
lista1[0] = 100  # Modificar elementos de una lista

# append
lista1.append(5)
print(lista1)

# count
print(f'El numero 2 se repite {lista1.count(2)} veces en la lista 1')

# extend
lista_extendida = [50, 51]
lista1.extend(lista_extendida)
print(lista1)

# index - Determinar si un valor se encuentra dentro de una lista, de ser asi retorna el indice
print(lista1.index(51))

# insert - Agregar elementos en cualquier posición
lista1.insert(0, 5000)  # Inserta un valor en el índice especificado
print(lista1)

# pop - Extrae elementos de la lista y retornarlos
print(lista1.pop(1))

# remove
lista1.remove(5000)

# reverse - da la vuelta a la lista
lista1.reverse()
print(lista1)

# sort - organiza la lista de menor a mayor
lista1.sort()
print(lista1)

# clear
# print(lista1.clear())


# lista2 = list((1,2,3))
# print(lista2)
