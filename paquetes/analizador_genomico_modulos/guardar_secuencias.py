"""
guardar_secuencias.py
Este script toma un archivo FASTA y guarda un archivo de texto tabulado (.tsv)
con dos columnas: ID de secuencia y la secuencia completa.
"""

from fasta_utils import leer_fasta

entrada = "data/secuencias.fasta"
salida = "output/secuencias.tsv"

secuencias = leer_fasta(entrada)

with open(salida, 'w') as f:
    f.write("ID\tSecuencia\n")
    for id_seq, secuencia in secuencias.items():
        f.write(f"{id_seq}\t{secuencia}\n")

print(f"[OK] Archivo generado: {salida}")
