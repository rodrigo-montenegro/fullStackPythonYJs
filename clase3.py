nombre = input("Nombre :")
print("Hola, " + nombre)
print(f"Bienvenido, {nombre}")

num = int(input("Numero :"))
if num > 0:
    print(f'Numero {num} positivo')
elif num < 0:
    print(f'Numero {num} negativo')
else:
    print("Numero es 0")
