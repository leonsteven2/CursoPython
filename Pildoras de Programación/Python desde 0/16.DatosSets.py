'''Los sets guardan datos, pero no estarán siempre ordenados
No permiten duplicar datos
Es mutable
Permite identificar si un objeto pertenece a un conjunto de elementos
'''
# Declaration
mi_set = {1, 2, 3, 4, 5}
print(mi_set)

mi_set2 = set()
mi_set2.add(1)
mi_set2.add(2)
mi_set2.add(3)
mi_set2.add(3)
print(mi_set2)

lista1 = [1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5]  # No permiten duplicar datos
lista1_set = set(lista1)
print(lista1_set)

pertenece = 3 in lista1_set  # 3 pertenece al set?
print(pertenece)

# frozenset - Son sets que no se pueden modificar
frutas = {
    'manzana',
    'banano',
    'pera',
    'uva'
}

mi_frozenset = frozenset(frutas)
print(mi_frozenset)
