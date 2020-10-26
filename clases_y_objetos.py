class Vuelo():
    def __init__(self, numero, capacidad):
        self.numero = numero
        self.capacidad = capacidad
        self.pasajeros = []

    def agregarPasajeros(self, nombre):
        if not self.asientosDisponibles():
            return False
        self.pasajeros.append(nombre)
        return True

    def asientosDisponibles(self):
        return int(self.capacidad - len(self.pasajeros))


"""
vuelo288 = Vuelo(288, 300)
print(vuelo288.numero)
print(vuelo288.capacidad)
vuelo288.agregarPasajeros("Jose Rodriguez")
vuelo288.agregarPasajeros("Pablo Martinez")
print(vuelo288.pasajeros)
print(vuelo288.asientosDisponibles())
vuelo288.agregarPasajeros("Sofia Mancuello")
print(vuelo288.pasajeros)
print(vuelo288.asientosDisponibles())
"""
vuelo288 = Vuelo(288, 2)
personas = ["Rodrigo", "Facundo", "Harry"]

for unaPersona in personas:
    if vuelo288.agregarPasajeros(unaPersona):
        print(f"Se agrego {unaPersona} al vuelo numero {vuelo288.numero}")
    else:
        print(f"No se puedo agregar a {unaPersona} por exceso de capacidad")
