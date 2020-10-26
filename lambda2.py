personas = [
    {"nombre": "Harry", "casa": "Gryffindor"},
    {"nombre": "Cho", "casa": "Ravenclaw"},
    {"nombre": "Draco", "casa": "Slytherin"}

]


def f(unaPersona):
    return unaPersona["nombre"]


# personas.sort(key=f)

personas.sort(key=lambda unaPersona: unaPersona["casa"])

print(personas)
