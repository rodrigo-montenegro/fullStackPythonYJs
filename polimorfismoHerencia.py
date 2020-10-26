class Ave:
    def introduccion(self):
        print("Existen muchos tipos de aves")

    def vuelo(self):
        print("Algunas aves pueden volar y otras no")


class Perico(Ave):
    def vuelo(self):
        print("Los pericos pueden volar")


class Pinguino(Ave):
    def vuelo(self):
        print("Los pinguinos no pueden volar")


unAve = Ave()
unPerico = Perico()
unPinguino = Pinguino()

unAve.introduccion()
unAve.vuelo()

unPerico.introduccion()
unPerico.vuelo()

unPinguino.introduccion()
unPinguino.vuelo()
