import pandas as pd


def leer_red_interaccion(ruta_archivo):
    """
    Lee un archivo de interacción regulatoria, ignorando comentarios (#),
    y convierte los valores vacíos en ".".
    """
    with open(ruta_archivo, "r") as archivo:
        lineas = archivo.readlines()

    # Eliminar comentarios
    lineas = [linea for linea in lineas if not linea.startswith("#")]

    # Separar encabezado y datos
    encabezado = lineas[0].strip().split("\t")
    datos = [linea.strip().split("\t") for linea in lineas[1:]]

    # Reemplazar valores vacíos con "."
    datos = [[campo if campo != "" else "." for campo in fila] for fila in datos]

    # Crear DataFrame
    df = pd.DataFrame(datos, columns=encabezado)
    return df


def calcular_estadisticas(df, salida="output.txt"):
    """
    Calcula estadísticas de la red y las guarda en un archivo.
    Elimina duplicados de la relación Regulador - Gen regulado.
    """
    regulador_col = df.columns[1]  # segunda columna
    gen_col = df.columns[4]        # quinta columna

    # Eliminar duplicados en la relación Regulador - Gen
    df_sin_repetidos = df[[regulador_col, gen_col]].drop_duplicates()

    total_reguladores = df_sin_repetidos[regulador_col].nunique()
    total_genes_regulados = df_sin_repetidos[gen_col].nunique()

    genes_por_regulador = (
        df_sin_repetidos.groupby(regulador_col)[gen_col]
        .nunique()
        .sort_values(ascending=False)
    )

    # Escribir salida
    with open(salida, "w") as f:
        f.write("📊 Estadísticas de la red de interacción\n")
        f.write(f"🔹 Total de reguladores: {total_reguladores}\n")
        f.write(f"🔹 Total de genes regulados: {total_genes_regulados}\n\n")
        f.write("🔸 Genes regulados por cada regulador:\n")
        for regulador, cantidad in genes_por_regulador.items():
            f.write(f"{regulador}: {cantidad}\n")


def main():
    archivo = "NetworkRegulatorGene.txt"
    df_red = leer_red_interaccion(archivo)
    calcular_estadisticas(df_red)


if __name__ == "__main__":
    main()

