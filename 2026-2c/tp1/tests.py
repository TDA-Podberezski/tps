import unittest

from tp1_2 import main as invictos


def _normalizar(invictas):
    # el orden interno no debe importar para comparar (se conservan duplicados)
    return sorted(invictas)


class TestInvictos(unittest.TestCase):

    def test_conjunto_vacio(self):
        invictas, cantidad = invictos([])
        self.assertEqual(invictas, [])
        self.assertEqual(cantidad, 0)

    def test_un_solo_punto(self):
        invictas, cantidad = invictos([(3, 7)])
        self.assertEqual(_normalizar(invictas), [(3, 7)])
        self.assertEqual(cantidad, 1)

    def test_ejemplo_del_enunciado(self):
        entrada = [(3, 4), (1, 5), (4, 2), (2, 2), (5, 1), (4, 5)]
        invictas, cantidad = invictos(entrada)

        self.assertEqual(_normalizar(invictas), [(4, 2), (4, 5), (5, 1)])
        self.assertEqual(cantidad, 3)


if __name__ == "__main__":
    unittest.main()
