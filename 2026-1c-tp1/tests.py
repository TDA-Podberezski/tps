import unittest
from tp1_1 import main as turnos
from tp1_3 import main as cajas

class TestTurnos(unittest.TestCase):
    def test_turnos_1(self):
        # Caso facil: no hay superposiciones, puedo atender primero al primer turno y luego al segundo
        orden, ganancia = turnos([(1, 10), (2, 10)])
        self.assertEqual(orden, [0, 1])
        self.assertEqual(ganancia, 20)



class TestCajas(unittest.TestCase):
    def test_cajas_1(self):
        # Caso facil: una sola caja, tiene altura 1, el orden es la unica caja con base 1 y altura 1
        altura, orden = cajas([(1, 1, 1)])
        self.assertEqual(altura, 1)
        self.assertEqual(orden, [0, (1, 1)])

if __name__ == "__main__":
    unittest.main()
