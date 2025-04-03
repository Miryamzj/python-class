secuencias = input ("Dame secuencias separadas por comas").split (",")
    
codones_de_inicio = [secuencia.strip()[:3] for secuencia in secuencias]

print (codones_de_inicio)