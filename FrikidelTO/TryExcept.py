from time import time

asd = "asd"

# El siguiente código funciona para to do tipo de error
try:
    int(asd)
except ValueError:
    print("No es possible")

# El siguiente code funciona solo para el error ValueError
try:
    x = 5 / 0
except ValueError:
    print("No es posible")
except ZeroDivisionError:
    print("No se puede dividir para 0")
except:
    print("ERROR DESCONOCIDO")

# Si se cumple las condiciones de try y no pasa por las excepciones se ejecutara else
try:
    x = 5 / 23
except:
    print("ERROR DESCONOCIDO")
else:
    print("Se cumplió try")

# Finally se ejecutara si o si
try:
    x = 5 / 0
except:
    print("ERROR DESCONOCIDO")
finally:
    print("Esto se ejecutara si o si")

time()


def calculator():
    pass


calculator()
