import datetime

print("Test ")
print("Hola, bienvenidos al curso del PoloTic")

x = 2.55e2
print(x)
miNumeroComplejo = 3 + 4j
print("Parte real de 3 + 4j:", miNumeroComplejo.real)
print("Parte imaginaria de 3 + 4j:", miNumeroComplejo.imag)
print(type(miNumeroComplejo))

miBoolean = 1 > 2
print(miBoolean)

miCadena = "Python es un gran lenguaje"
print(miCadena)

fecha = datetime.datetime.now()
print(fecha)

diaMesAño = str(datetime.datetime.now().date())
print(diaMesAño)
