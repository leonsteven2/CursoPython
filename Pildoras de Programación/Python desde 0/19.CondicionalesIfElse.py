edad = 12

if edad >= 18:
    print("Es mayor de edad")
elif 13 <= edad <= 17:
    print("Es joven")
else:
    print("Es menor de edad")

# Forma mas elegante - Operador ternario
mensaje = ""
mensaje = "Usted es mayor de edad" if edad >= 18 else "Usted es menor de edad"
print(mensaje)
