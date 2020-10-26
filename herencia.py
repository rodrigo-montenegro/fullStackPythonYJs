class Empleado():
    numEmpleado = 0
    porcentajeAumento = 1.04

    def __init__(self, nombre, apellido, sueldo):
        self.nombre = nombre
        self.apellido = apellido
        self.sueldo = sueldo
        self.email = str(nombre + '.' + apellido + '@miempresa.com')
        Empleado.numEmpleado += 1

    def nombreCompleto(self):
        return '{}{}'.format(self.nombre, self .apellido)

    def aplicarAumentoSueldo(self):
        self.sueldo = int(self.sueldo * self.porcentajeAumento)

# Clase heredada


class Desarrollador(Empleado):
    porcentajeAumento = 1.10

    def __init__(self, nombre, apellido, sueldo, lenguaje):
        super().__init__(nombre, apellido, sueldo)
        self.lenguaje = lenguaje


empleado1 = Desarrollador("Harry", "Potter", 999, "Python")
print(empleado1.email.lower())
empleado2 = Empleado("Ron", "Weasley", 999)
print(
    f"El numero del empleado {empleado2.apellido} es :{empleado2.numEmpleado}")
empleado1.aplicarAumentoSueldo()
print(f"El nuevo sueldo de {empleado1.apellido} es : {empleado1.sueldo}")
empleado2.aplicarAumentoSueldo()
print(f"El nuevo sueldo de {empleado2.apellido} es : {empleado2.sueldo}")
print(f"El lenguaje que maneja {empleado1.apellido} es {empleado1.lenguaje}")
