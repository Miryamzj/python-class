secuencias = input ("Dame secuencias separadas por comas").upper().split(",")
conteo = [(f"A: {secuencia.count('A')}", f"T: {secuencia.count('T')}", f"G: {secuencia.count('G')}", f"C: {secuencia.count('C')}") for secuencia in secuencias]
print(conteo)