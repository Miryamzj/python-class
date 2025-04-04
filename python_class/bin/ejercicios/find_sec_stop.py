#pedimos al usuario ingresar secuencias de DNA
secuencias = input ("Dame secuencias separadas por comas").split(",")
#indicamos cuáles son las secuencias de paro que hay que reconocer
secuencias_stop = [ secuencia for secuencia in secuencias if "TAA" in secuencia or "TAG" in secuencia or "TGA" in secuencia]

print (secuencias_stop)

