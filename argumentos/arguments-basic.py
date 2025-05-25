import argparse
#creamos al parser

parser =argparse.ArgumentParser(
    description="Programa que dice hola",
    epilog= "Fin del programa")

parser.add_argument("nombre", help= "nombre de la  persona")
args= parser.parse_args()

print(args)

print(f"El nombre  del usuario es {args.nombre}")