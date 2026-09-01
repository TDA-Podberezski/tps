import unittest

from tp1_2 import main as invictos
from tp1_1 import main as lavarropas


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

class TestLavarropas(unittest.TestCase):

    def test_no_ropas(self):
        output = lavarropas("./tp1_files/vacio")

        self.assertEqual(output, [])

    def test_no_incompatibilidades(self):
        output = lavarropas("./tp1_files/no_incompatibilidades")

        etiquetas = [x[1] for x in output]
        self.assertEqual(len(set(etiquetas)), 1)


    def test_caso_basico(self):
        output = lavarropas("./tp1_files/enunciado")
        etiquetas = [x[1] for x in output]

        self.assertEqual(len(set(etiquetas)), 2)


if __name__ == "__main__":
    unittest.main()
