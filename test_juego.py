import unittest
from juego import comparar_resultado

class TestJuego(unittest.TestCase):
    def test_piedra_vs_tijera(self):
        self.assertEqual(comparar_resultado('piedra', 'tijera'), 1)

    def test_piedra_vs_papel(self):
        self.assertEqual(comparar_resultado('piedra', 'papel'), -1)

    def test_piedra_vs_piedra(self):
        self.assertEqual(comparar_resultado('piedra', 'piedra'), 0)

    def test_tijera_vs_papel(self):
        self.assertEqual(comparar_resultado('tijera', 'papel'), 1)

    def test_tijera_vs_piedra(self):
        self.assertEqual(comparar_resultado('tijera', 'piedra'), -1)

    def test_tijera_vs_tijera(self):
        self.assertEqual(comparar_resultado('tijera', 'tijera'), 0)

    def test_papel_vs_piedra(self):
        self.assertEqual(comparar_resultado('papel', 'piedra'), 1)

    def test_papel_vs_tijera(self):
        self.assertEqual(comparar_resultado('papel', 'tijera'), -1)

    def test_papel_vs_papel(self):
        self.assertEqual(comparar_resultado('papel', 'papel'), 0)

if __name__ == '__main__':
    unittest.main()