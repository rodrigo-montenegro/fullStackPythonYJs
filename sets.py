# Los sets no permiten elementos repetidos.

conjunto = set()
conjunto.add(1.0)
conjunto.add(2.0)
conjunto.add(3.0)
conjunto.add(1.0)
print(conjunto)
conjunto.remove(2.0)
print(conjunto)
print(f"El conjunto {conjunto} tiene {len(conjunto)} elementos")
