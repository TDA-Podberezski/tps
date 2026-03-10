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
        # Caso facil: una sola caja 10 veces se apila 10 veces
        orden = cajas([(1, 1, 1, 10)])
        self.assertEqual(orden, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

if __name__ == "__main__":
    unittest.main()
