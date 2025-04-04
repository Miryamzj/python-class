#pedimos al usuario ingresar secuencias separadas 
secuencias = input ("Dame secuencias separadas por comas").split (",")
#las primeras 3 letras serán los codones de incio     
codones_de_inicio = [secuencia.strip()[:3] for secuencia in secuencias]

print (codones_de_inicio)