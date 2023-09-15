lista_nombre = ['edward', 'carlos', 'viviana']
for nombre in lista_nombre:
    print(nombre)

tupla_notas = ('edward', 30, 4.5)
for nota in tupla_notas:
    print(nota)

set_departamentos = {'ventas','compras','redes','it'}
for departamento in set_departamentos:
    print(departamento)

for i in range(4): # _ significa que no hay variable
    print(i+1)

for indice, valor in enumerate(lista_nombre):
    print(indice, valor)