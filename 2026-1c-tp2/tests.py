import unittest
from tp2_1 import main as dojo
from tp2_2 import main as contenedores

class TestDojo(unittest.TestCase):
    def test_dojo_1(self):
        s1 = 1
        s2 = 4
        relaciones = [(1, 2, 10), (1, 3, 1), (2, 3, 1), (2, 4, 1), (3, 4, 3)]
        dojoSolucion = dojo(s1, s2, relaciones)
        dojoEsperado = ({1, 2}, {3, 4})
        self.assertEqual(dojoSolucion, dojoEsperado)


class TestContenedores(unittest.TestCase):
    def test_contenedores_1(self):
        productos = [(2, 10), (5, 10), (7, 20)]
        contenedoresEsperados = [{0, 1}, {2}]
        Ganancia, containersSolucion = contenedores(productos, k=2, C=8, a=5)
        self.assertEqual(Ganancia, 30)
        self.assertEqual(containersSolucion, contenedoresEsperados)


if __name__ == "__main__":
    unittest.main()
