import sys

try:
    numero1 = int(input("Ingrese numero 1:"))
    numero2 = int(input("Ingrese numero 2:"))
except ValueError:
    print("Valor no valido.")
    sys.exit(1)
try:
    resultado = numero1/numero2
    error = 0
except ZeroDivisionError:
    print("Error. No se puede dividir por cero.")
    error = 1
finally:
    print(f"Mensaje de Error= {error}")

print(f"El resultado de la operacion {numero1}/{numero2}={resultado}")
