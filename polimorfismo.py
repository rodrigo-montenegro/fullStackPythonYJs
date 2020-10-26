class Tomate():
    def tipo(self):
        print("Vegetal")

    def color(self):
        print("Rojo")


class Manzana():
    def tipo(self):
        print("Fruta")

    def color(self):
        print("Verde")

# Funcion generica que recibe el objeto


def funcion(obj):
    obj.tipo()
    obj.color()


unTomate = Tomate()
unaManzana = Manzana()

funcion(unTomate)
funcion(unaManzana)
