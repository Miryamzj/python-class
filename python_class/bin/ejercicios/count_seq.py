inputfile = "dna_sequences.fasta"

with open (inputfile,"r") as infile:
    lineas = infile.readlines()

lineas_filtradas = [linea for linea in lineas if linea.startswith(">")]
print (f"total de secuencias: {len(lineas_filtradas)}")