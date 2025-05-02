def validar_secuencia(secuencia):
    bases_validas = {"A", "T", "G", "C"}
    return all(base in bases_validas for base in secuencia)
