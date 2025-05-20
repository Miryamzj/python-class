import os

def cargar_genoma(fasta_path):
    #Cargamos el genoma desde el archivo FASTA y lo retorna como una cadena.
    if not os.path.exists(fasta_path):
        raise FileNotFoundError(f"Archivo FASTA no encontrado: {fasta_path}")
    
    with open(fasta_path, 'r') as f:
        lineas = f.readlines()
    
    secuencia = ''.join(linea.strip() for linea in lineas if not linea.startswith('>'))
    return secuencia