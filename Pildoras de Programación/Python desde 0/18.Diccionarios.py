# Utilizan el concepto clave - valor
# Los diccionarios son mutables
# Las claves deben ser inmutables (no cambian su valor)

# Primera forma de declaración
mi_diccionario = {
    'Edward': [1.4, 4.5, 5.0],
    'Carlos': [4.4, 5.0, 4.5],
    'Juan': [3.0, 3.5, 4.0]
}
print(mi_diccionario)

# Segunda forma de declaración
mi_diccionario2 = dict(Edward=[1.4, 4.5, 5.0],
                       Carlos=[4.4, 5.0, 4.5],
                       Juanca=[3.0, 3.5, 4.0])
print(mi_diccionario2)

# Tercera forma de declaración
mi_diccionario3 = dict()
mi_diccionario3['Edward'] = [1.4, 4.5, 5.0]
mi_diccionario3['Carlos'] = [4.4, 5.0, 4.5]
mi_diccionario3['Juan'] = [3.0, 3.5, 4.0]
print(mi_diccionario3)

# Acceder a su valor
print(mi_diccionario['Edward'])

# Borrar elemento
del mi_diccionario['Carlos']
print(mi_diccionario)

# keys
print(mi_diccionario.keys())
# values
print(mi_diccionario.values())
# both
print(mi_diccionario.items())
