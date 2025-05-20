import os

def leer_archivo_picos(peaks_path):
    #Lee un archivo TSV de picos y devuelve una lista de diccionarios con TF_name, Peak_start y Peak_end."""
    if not os.path.exists(peaks_path):
        raise FileNotFoundError(f"Archivo de picos no encontrado: {peaks_path}")

    picos = []
    with open(peaks_path, 'r') as f:
        next(f)  # Saltar encabezado
        for linea in f:
            campos = linea.strip().split('\t')
            try:
                tf = campos[2]
                start = int(float(campos[3]))
                end = int(float(campos[4]))
                picos.append({'TF_name': tf, 'Peak_start': start, 'Peak_end': end})
            except (IndexError, ValueError) as e:
                print(f"[Advertencia] Línea ignorada: {linea.strip()} - Error: {e}")
                continue
    return picos


def extraer_secuencias(peaks_data, genoma):
    #Extrae secuencias del genoma para cada TF según las coordenadas de picos.
    secuencias_por_tf = {}
    largo_genoma = len(genoma)

    for pico in peaks_data:
        tf = pico['TF_name']
        start = pico['Peak_start']
        end = pico['Peak_end']

        if start < 0 or end > largo_genoma or start >= end:
            print(f"[Advertencia] Coordenadas fuera de rango: {tf} ({start}, {end})")
            continue

        secuencia = genoma[start:end]
        secuencias_por_tf.setdefault(tf, []).append(secuencia)

    return secuencias_por_tf