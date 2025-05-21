import os
from genome import cargar_genoma
from peaks import leer_archivo_picos, extraer_secuencias
from io_utils import guardar_fasta_por_tf

def main():
    # Rutas relativas desde la carpeta del programa 
    # Con base_dir y os, ya se construyen rutas relativas al programa, sin importar desde qué carpeta lo ejecute
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(base_dir, "data")
    output_dir = os.path.join(base_dir, "output")

    genome_path = os.path.join(data_dir, "ecoli_genome.fasta")
    peaks_path = os.path.join(data_dir, "union_peaks_file.tsv")

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