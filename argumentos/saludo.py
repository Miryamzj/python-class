import argparse

# 1. Crear el parser
parser = argparse.ArgumentParser(description="Saluda a una persona")

# 2. Definir los argumentos -- argumento posicional
parser.add_argument("nombre", help="Nombre de la persona a saludar")

# 3. Leer/Procesar el argumento dado por el usuario
args = parser.parse_args()

# Usar el argumento
print(f"Hola, {args.nombre} (•‿•) !")
