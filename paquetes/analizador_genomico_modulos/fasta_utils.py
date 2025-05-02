from pathlib import Path

def leer_fasta(ruta_fasta):
    ruta = Path(ruta_fasta)
    if not ruta.is_file():
        print(f"[ERROR] No se encontró el archivo: {ruta_fasta}")
        return {}
    secuencias = {}
    id_actual = None
    with open(ruta_fasta, 'r') as f:
        for linea in f:
            linea = linea.strip()
            if linea.startswith('>'):
                id_actual = linea[1:].strip()
                secuencias[id_actual] = ''
            else:
                if id_actual:
                    secuencias[id_actual] += linea.upper()
    return secuencias
