from .tp1_1 import main as turnos


def test_1():
    # Caso facil: no hay superposiciones, puedo atender primero al primer turno y luego al segundo
    orden, ganancia= turnos([(1, 10), (2, 10)])
    assert orden == [0, 1]
    assert ganancia == 20
