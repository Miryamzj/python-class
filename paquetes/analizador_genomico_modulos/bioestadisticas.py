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
