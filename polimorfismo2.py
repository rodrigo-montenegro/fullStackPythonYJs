class Argentina():
    def capital(self):
        print("Buenos Aires")

    def idioma(self):
        print("Español")


class EEUU():
    def capital(self):
        print("Waashington DC")

    def idioma(self):
        print("English")


paisArgentina = Argentina()
paisEEUU = EEUU()

for unPais in (paisArgentina, paisEEUU):
    unPais.capital()
    unPais.idioma()
