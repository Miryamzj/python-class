"""
==================================================
🧬 Analizador de Secuencias Genéticas - FASTA
==================================================

Este programa permite analizar secuencias de genes almacenadas en un archivo
FASTA. Realiza lo siguiente:

✅ Lee el archivo FASTA
✅ Verifica que las secuencias contengan solo bases A, T, G, C
✅ Calcula frecuencia de bases
✅ Calcula contenido GC
✅ Exporta resultados a un archivo .tsv

🔧 Requisitos:
- El archivo de entrada debe estar en: data/secuencias.fasta
- Los resultados se guardan en: salida/resultados.tsv

▶️ Ejecución:

    python analizador.py

Autor: Tu Nombre
Fecha: 2025

--------------------------------------------------
"""

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


def validar_secuencia(secuencia):
    bases_validas = {"A", "T", "G", "C"}
    return all(base in bases_validas for base in secuencia)


def contar_bases(secuencia):
    bases = {"A": 0, "T": 0, "G": 0, "C": 0}
    for base in secuencia:
        if base in bases:
            bases[base] += 1
    return bases


def calcular_gc(secuencia):
    total = len(secuencia)
    if total == 0:
        return 0.0
    g = secuencia.count("G")
    c = secuencia.count("C")
    return round((g + c) / total * 100, 2)


def exportar_tsv(resultados, ruta_salida):
    salida = Path(ruta_salida)
    salida.parent.mkdir(parents=True, exist_ok=True)

    with open(ruta_salida, 'w') as f:
        f.write("ID\tLongitud\tA\tT\tG\tC\tGC%\n")
        for gen_id, datos in resultados.items():
            f.write(f"{gen_id}\t{datos['longitud']}\t{datos['A']}\t{datos['T']}\t{datos['G']}\t{datos['C']}\t{datos['GC%']}\n")


# --- Inicio del programa ---
ruta_entrada = "data/secuencias.fasta"
ruta_salida = "salida/resultados.tsv"

secuencias = leer_fasta(ruta_entrada)

if not secuencias:
    print("[INFO] No se procesó ninguna secuencia.")
else:
    resultados = {}
    for gen_id, sec in secuencias.items():
        if not validar_secuencia(sec):
            print(f"[ADVERTENCIA] La secuencia del gen '{gen_id}' contiene bases no válidas y será omitida.")
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
        print("[INFO] No se generaron resultados válidos para exportar.")

print (f"__name__ vale: {__name__}")

# --- Pruebas simples con assert para verificar funciones clave ---
assert contar_bases("ATGC") == {"A": 1, "T": 1, "G": 1, "C": 1}, "Error en contar_bases()"
assert calcular_gc("ATGC") == 50.0, "Error en calcular_gc()"
assert validar_secuencia("ATGC") is True, "Error en validar_secuencia() con secuencia válida"
assert validar_secuencia("ATGN") is False, "Error en validar_secuencia() con caracteres inválidos"

