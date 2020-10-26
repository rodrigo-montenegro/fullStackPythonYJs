try:
    f = open("archivoejemplo.txt")
    f.write("Linea de prueba dentro del archivo.")
except:
    print("Algo paso al intentar abrir el archivo.")
finally:
    f.close()
