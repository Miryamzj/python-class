inputfile = "4_input_adapters.txt"
outputfile = "4_input_no_adapters.txt"

#Abrir y Leer el archivo de entrada 4_input_adapters.txt
with open (inputfile,"r") as infile, open(outputfile, "w") as outfile:
    for linea in infile: 
        #Cortar adaptadores de la secuencia 4_input_adapters.txt. Los adaptadores son los primeros 1-14 caracteres de cada secuencia.
        secuencia_limpia = linea.strip ()[14:]

        #Manda la salida a un archivo 4_input_no_adapters.txt
        outfile.write(f"{secuencia_limpia}\n")

    #print (secuencia_limpia, file = outfile, end="\n")
    
