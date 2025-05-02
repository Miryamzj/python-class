# 📋 Detalles del Proyecto: Analizador Genómico

## 🎯 Objetivo

Desarrollar una herramienta en Python que permita analizar secuencias genéticas almacenadas en un archivo en formato FASTA.

El programa debe:

- Leer el archivo FASTA y extraer las secuencias por ID
- Calcular la frecuencia de bases A, T, C y G en cada secuencia
- Calcular el contenido porcentual de GC
- Generar un resumen con la longitud de cada secuencia
- Exportar los resultados a un archivo `.tsv` y/o `.json`

## 📂 Formatos de Entrada y Salida

### 🔹 Formato de entrada: archivo FASTA

El archivo debe tener la extensión `.fasta` y contener secuencias en el siguiente formato:

```
>gene1
ATGCGTACGTAGCT
>gene2
TTGACCGTA
```

- Cada secuencia comienza con una línea de encabezado que inicia con `>` seguida del identificador del gen.
- Las secuencias pueden ocupar una o varias líneas, pero en este caso se espera una línea por secuencia.

---

### 🔸 Formato de salida: archivo `.tsv`

El programa genera un archivo llamado `resultados.tsv` con el siguiente contenido:

```
ID      Longitud    A   T   G   C   GC%
gene1   14          3   3   4   4   57.14
gene2   9           2   3   2   2   44.44
```

Cada fila contiene:

- ID del gen
- Longitud total de la secuencia
- Conteo de bases A, T, G, C
- Porcentaje de contenido GC

## ⚠️ Errores comunes y validaciones

El programa incluye validaciones básicas para mejorar la calidad de los datos:

### ❌ Bases inválidas

Si una secuencia contiene caracteres distintos de A, T, G o C (por ejemplo, N, R, Y, etc.), se mostrará un mensaje como este y se omitirá esa secuencia del análisis:

```
[ADVERTENCIA] La secuencia del gen 'gene3' contiene bases no válidas y será omitida.
```

### ❌ Archivo de entrada no encontrado

Si el archivo `data/secuencias.fasta` no existe, el programa mostrará:

```
[ERROR] No se encontró el archivo: data/secuencias.fasta
```

### ℹ️ Sin resultados válidos

Si todas las secuencias son inválidas o el archivo está vacío:

```
[INFO] No se generaron resultados válidos para exportar.
```

Estas validaciones ayudan a que el programa sea más robusto y fácil de usar.


## 📦 Estructura Inicial del Proyecto

```text
analizador_genomico/
├── data/
│   └── secuencias.fasta         ← Archivo de entrada
├── salida/                      ← Carpeta vacía para guardar resultados
├── analizador.py                ← Código fuente principal con todas las funciones
├── README.md                    ← Instrucciones de uso del programa
└── detalles_proyecto.md         ← Este documento con la descripción general
```

## 💡 Futuras mejoras

- Modularizar el código en archivos separados (módulos)
- Convertir en un paquete reutilizable
- Agregar interfaz por línea de comandos (`argparse`)
- Añadir filtros por tamaño mínimo o %GC
