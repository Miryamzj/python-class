"""
analizador.py
Script principal que coordina el análisis de secuencias FASTA usando el paquete `analizador`.
"""

from fasta_utils import leer_fasta
from validador import validar_secuencia
from bioestadisticas import contar_bases, calcular_gc
from exportador import exportar_tsv

# --- Configuración de entrada y salida ---
ruta_entrada = "data/secuencias.fasta"
ruta_salida = "output/resultados.tsv"

# --- Leer las secuencias ---
secuencias = leer_fasta(ruta_entrada)

if not secuencias:
    print("[INFO] No se procesó ninguna secuencia.")
else:
    resultados = {}

    for gen_id, sec in secuencias.items():
        if not validar_secuencia(sec):
            print(f"[ADVERTENCIA] El gen '{gen_id}' contiene bases no válidas y será omitido.")
            continue

        bases = contar_bases(sec)
        gc = calcular_gc(sec)

        resultados[gen_id] = {
            "longitud": len(sec),
            "A": bases["A"],
            "T": bases["T"],
            "G": bases["G"],
            "C": bases["C"],
            "GC%": gc
        }

    if resultados:
        exportar_tsv(resultados, ruta_salida)
        print(f"[OK] Resultados guardados en: {ruta_salida}")
    else:
        print("[INFO] No se generaron resultados válidos.")
