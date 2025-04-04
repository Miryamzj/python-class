#le damos un archivo de entrada como un input
inputfile = "dna_sequences.txt"
outputfile = "dna_sequences.fasta"

#Lee el archivo de entrada dna_sequences.txt y generamos un archivo de salida 
with open (inputfile,"r") as infile, open(outputfile,"w") as outfile:
    for linea in infile: 
        id, seq = linea.strip().split("\t")
        outfile.write(f">{id}\n{seq.upper()}\n")

    