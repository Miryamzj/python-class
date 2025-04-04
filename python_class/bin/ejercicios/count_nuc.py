#Pide al usuario que ingrese varias secuencias de ADN separadas por comas
secuencias = input ("Dame secuencias separadas por comas").upper().split(",")
#usamos el método count para contar cada letra en cada secuencia
conteo = [(f"A: {secuencia.count('A')}", f"T: {secuencia.count('T')}", f"G: {secuencia.count('G')}", f"C: {secuencia.count('C')}") for secuencia in secuencias]
print(conteo)