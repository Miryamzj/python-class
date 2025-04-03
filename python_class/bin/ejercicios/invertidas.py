secuencias = input ("Dame secuencias separadas por comas").split(",")

secuencias_invertidas=[secuencia.strip()[::-1] for secuencia in secuencias]

print (secuencias_invertidas)