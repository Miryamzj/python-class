import argparse

def leer_secuencia_desde_archivo(ruta):
    """
    Lee una secuencia de ADN desde un archivo de texto.
    Retorna la secuencia como una cadena sin espacios ni saltos de línea.
    """
    with open(ruta, "r") as archivo:
        secuencia = archivo.read().strip()
    return secuencia


def calcular_contenido_at(secuencia):
    """
    Calcula el contenido de AT (adenina + timina) en una secuencia de ADN.
    Devuelve el valor como proporción entre 0 y 1.
    """
    secuencia = secuencia.upper()
    total = len(secuencia)
    conteo_a = secuencia.count('A')
    conteo_t = secuencia.count('T')
    contenido_at = (conteo_a + conteo_t) / total
    return contenido_at


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Calcula el contenido de AT en una secuencia.")
    parser.add_argument("input", help="Archivo de entrada con la secuencia")
 
    args = parser.parse_args()

    # Ruta del archivo de entrada
    archivo_entrada = args.input

    # Leer la secuencia y calcular el contenido de AT
    secuencia = leer_secuencia_desde_archivo(archivo_entrada)
    contenido_at = calcular_contenido_at(secuencia)

    print(f"Contenido de AT: {contenido_at:.2%}")


