# AVANCE PROYECTO FINAL-INCISO A

import os


def cargar_genoma(fasta_path):
    #Carga el genoma desde el archivo FASTA y lo retorna como una cadena de texto.
    if not os.path.exists(fasta_path):
        raise FileNotFoundError(f"Archivo FASTA no encontrado: {fasta_path}")

    with open(fasta_path, 'r') as f:
        lineas = f.readlines()
    
    secuencia = ''.join(linea.strip() for linea in lineas if not linea.startswith('>'))
    return secuencia


def leer_archivo_picos(peaks_path):
    """Lee un archivo TSV de picos y devuelve una lista de diccionarios con TF_name, Peak_start y Peak_end."""
    if not os.path.exists(peaks_path):
        raise FileNotFoundError(f"Archivo de picos no encontrado: {peaks_path}")

    picos = []
    with open(peaks_path, 'r') as f:
        next(f) #salto encabezado
       # encabezado = f.readline().strip().split('\t')
       # print("[DEBUG] Encabezado leído:", encabezado)
        #idx_tf = encabezado.index('TF_name')
        #dx_start = encabezado.index('Peak_start')
        #idx_end = encabezado.index('Peak_end')

        for linea in f:
            campos = linea.strip().split('\t')
    

            try:
                 tf = campos[2]
                 start = int(float(campos[3]))
                 end = int(float(campos[4]))
                 picos.append({'TF_name': tf, 'Peak_start': start, 'Peak_end': end})
            except (IndexError, ValueError) as e:
                 print(f"[Advertencia] Línea ignorada por formato incorrecto: {linea.strip()}")
                 print(f"           Error: {e}")
                 print(f"           Campos detectados: {campos}")
                 continue #Seguimos con la siguiente línea e ignoramos las problemáticas
    return picos 

def extraer_secuencias(peaks_data, genoma):
    #Agrupa las secuencias extraídas por TF_name en un diccionario.
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
        if tf not in secuencias_por_tf:
            secuencias_por_tf[tf] = []
        secuencias_por_tf[tf].append(secuencia)

    return secuencias_por_tf


def guardar_fasta_por_tf(secuencias_por_tf, output_dir):
    #Guarda archivos FASTA separados por cada TF_name en el directorio especificado.
    os.makedirs(output_dir, exist_ok=True)

    for tf, secuencias in secuencias_por_tf.items():
        filename = os.path.join(output_dir, f"{tf}.fa")
        with open(filename, 'w') as f:
            for i, sec in enumerate(secuencias):
                f.write(f">{tf}_peak_{i+1}\n")
                f.write(f"{sec}\n")

        print(f"[INFO] Archivo generado: {filename}")


def main():
    #Guardo las rutas fijas (para pruebas locales).

    peaks_path = r"C:\\Users\\HP\\Desktop\\Licenciatura_en_Ciencias_Genomicas\\Segundo_semestre\\Python\\python-class\\peak_analysis-main\\data\\union_peaks_file.tsv"
    genome_path = r"C:\\Users\\HP\\Desktop\\Licenciatura_en_Ciencias_Genomicas\\Segundo_semestre\\Python\\python-class\\peak_analysis-main\\data\\ecoli_genome.fasta"
    output_dir = r"C:\\Users\\HP\\Desktop\\Licenciatura_en_Ciencias_Genomicas\\Segundo_semestre\\Python\\python-class\\peak_analysis-main\\output"

    try:
        genoma = cargar_genoma(genome_path)
        picos = leer_archivo_picos(peaks_path)
        print(f"[DEBUG] Número de picos leídos: {len(picos)}")
        secuencias = extraer_secuencias(picos, genoma)
        print(f"[DEBUG] TFs detectados: {list(secuencias.keys())}")
        for tf, seqs in secuencias.items():
             print(f"[DEBUG] {tf} tiene {len(seqs)} secuencias")
        guardar_fasta_por_tf(secuencias, output_dir)
        print("[✔] Proceso completado correctamente.")
    except Exception as e:
        print(f"[ERROR] {e}")


if __name__ == "__main__":
    main()
