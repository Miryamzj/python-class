import os

def guardar_fasta_por_tf(secuencias_por_tf, output_dir):
    """Guarda archivos FASTA separados por TF en un directorio de salida."""
    os.makedirs(output_dir, exist_ok=True)

    for tf, secuencias in secuencias_por_tf.items():
        filename = os.path.join(output_dir, f"{tf}.fa")
        with open(filename, 'w') as f:
            for i, sec in enumerate(secuencias):
                f.write(f">{tf}_peak_{i+1}\n")
                f.write(f"{sec}\n")
        print(f"[INFO] Archivo generado: {filename}")