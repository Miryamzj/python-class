inputfile = "dna_sequences.txt"
outputfile = "dna_sequences.fasta"

#Lee el archivo de entrada dna_sequences.txt
with open (inputfile,"r") as infile, open(outputfile,"w") as outfile:
    for linea in infile: 
        id, seq = linea.strip().split("\t")
        outfile.write(f">{id}\n{seq.upper()}\n")

    