from analizador.fasta_utils import leer_fasta
from analizador.validador import validar_secuencia
from analizador.bioestadisticas import contar_bases, calcular_gc

def test_todo():
    assert contar_bases("ATGC") == {"A": 1, "T": 1, "G": 1, "C": 1}
    assert calcular_gc("GGCC") == 100.0
    assert validar_secuencia("ATGC") is True
    assert validar_secuencia("NNNN") is False
