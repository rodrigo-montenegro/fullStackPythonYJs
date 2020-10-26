# Decorators

def miMensaje(f):
    def wrapper():
        print("Esta funcion esta por comenzar")
        f()
        print("Mi funcion ha terminado")
    return wrapper


@miMensaje  # Es pasada como parametro f
def hola():
    for miNumero in range(5):
        print(miNumero)


hola()
