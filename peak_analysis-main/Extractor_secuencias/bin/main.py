import os
import argparse

# Importamos funciones definidas en otros módulos
from genome import cargar_genoma
from peaks import leer_archivo_picos, extraer_secuencias
from io_utils import guardar_fasta_por_tf
#Implementamos el uso de argumentos para su ejecución desde terminal
def parse_args():
    parser = argparse.ArgumentParser(description="Extrae secuencias FASTA para factores de transcripción en E. coli")
    parser.add_argument("--genoma", required=True, help="Ruta al archivo FASTA del genoma")
    parser.add_argument("--picos", required=True, help="Ruta al archivo TSV con coordenadas de picos")
    parser.add_argument("--salida", required=True, help="Directorio de salida para archivos FASTA")
    return parser.parse_args()

def main():
    args = parse_args()
    genome_path = args.genoma
    peaks_path = args.picos
    output_dir = args.salida

    try:
        genoma = cargar_genoma(genome_path)
        picos = leer_archivo_picos(peaks_path)
        print(f"[DEBUG] Picos leídos: {len(picos)}")
        secuencias = extraer_secuencias(picos, genoma)
        print(f"[DEBUG] TFs detectados: {list(secuencias.keys())}")
        guardar_fasta_por_tf(secuencias, output_dir)
        print("[✔] Proceso completado correctamente.")
    except Exception as e:
        print(f"[ERROR] {e}")

if __name__ == "__main__":
    main()
