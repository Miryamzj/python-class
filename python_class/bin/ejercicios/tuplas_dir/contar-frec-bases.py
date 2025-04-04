secuencia = tuple ("ATGCTTCGA")
print(secuencia.count("A"))

#otra forma
for base in "ACGT": 
    print(f"{secuencia.count(base)} bases {base}")