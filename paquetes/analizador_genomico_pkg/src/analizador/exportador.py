from pathlib import Path

def exportar_tsv(resultados, ruta_salida):
    salida = Path(ruta_salida)
    salida.parent.mkdir(parents=True, exist_ok=True)
    with open(ruta_salida, 'w') as f:
        f.write("ID\tLongitud\tA\tT\tG\tC\tGC%\n")
        for gen_id, datos in resultados.items():
            f.write(f"{gen_id}\t{datos['longitud']}\t{datos['A']}\t{datos['T']}\t{datos['G']}\t{datos['C']}\t{datos['GC%']}\n")
