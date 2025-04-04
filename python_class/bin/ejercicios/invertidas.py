#Pedimos al usuario ingresar secuencias para invertirlas después 
secuencias = input ("Dame secuencias separadas por comas").split(",")
#invertimos la secuencia con .strip()[::-1[]
secuencias_invertidas=[secuencia.strip()[::-1] for secuencia in secuencias]

print (secuencias_invertidas)