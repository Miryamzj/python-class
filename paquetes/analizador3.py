"""
analizador.py
Script principal para ejecutar el análisis genómico sin necesidad de instalar el paquete con pip.
"""

import sys
from pathlib import Path

# Añadir la carpeta 'src' al path para poder importar el paquete
sys.path.append(str(Path(__file__).resolve().parent / "src"))

from analizador.fasta_utils import leer_fasta
from analizador.validador import validar_secuencia
from analizador.bioestadisticas import contar_bases, calcular_gc
from analizador.exportador import exportar_tsv


def main():
    ruta_entrada = "data/secuencias.fasta"
    ruta_salida = "salida/resultados.tsv"

    secuencias = leer_fasta(ruta_entrada)

    if not secuencias:
        print("[INFO] No se procesó ninguna secuencia.")
        return

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


if __name__ == "__main__":
    main()
