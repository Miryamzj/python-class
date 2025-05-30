# Proyecto de Automatización para la Extracción de Secuencias FASTA desde Picos de Unión de Factores de Transcripción en *E. coli*

## LICENCIATURA EN CIENCIAS GENÓMICAS - Curso Programación en Python - 2025
## Miryam Zamora Jiménez
*** Proyecto: Extractor de secuencias - 2do Semestre

Este proyecto en Python automatiza la **extracción de secuencias FASTA** correspondientes a los picos de unión de distintos **factores de transcripción (TFs)** en el genoma de *Escherichia coli*, a partir de archivos de coordenadas generados por experimentos de tipo **ChIP-Seq**.

---

## Estructura del Proyecto

Extractor_secuencias/
├── bin/
│ ├── main.py # Script principal
│ ├── genome.py # Carga del archivo FASTA
│ ├── peaks.py # Lectura y manejo de picos
│ ├── io_utils.py # Guardado de archivos FASTA por TF
├── data/ # Archivos de entrada (.fasta, .tsv)
├── output/ # Archivos de salida generados
├── README.md
├── DETALLES_DEL_PROYECTO.md
├── .gitignore


---

## ¿Qué hace el programa?

1. Lee un archivo **FASTA** con el genoma completo de *E. coli*.  
2. Lee un archivo **TSV** con coordenadas de picos y el nombre del TF asociado.  
3. Extrae las secuencias correspondientes para cada pico.  
4. Guarda un archivo `.fa` por cada TF, conteniendo las secuencias de sus picos.

---
---

## Entradas

- `--genoma`: Ruta al archivo FASTA del genoma completo  
- `--picos`: Ruta al archivo `.tsv` con coordenadas y nombres de TFs  
- `--salida`: Carpeta donde se generarán los archivos `.fa` por TF

Formato esperado del archivo `.tsv`:


---

## Ejemplo de uso

Desde la raíz del proyecto:

```bash
python bin/main.py \
  --genoma data/ecoli_genome.fasta \
  --picos data/union_peaks_file.tsv \
  --salida output/

## Esto genera archivos como 
output/lexA.fa
output/arcA.fa
output/fnr.fa