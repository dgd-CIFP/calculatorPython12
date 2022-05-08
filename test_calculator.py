import unittest
import calculadora

class TestCalculator(unittest.TestCase):
	def test_calculator12(self):
		resultado_suma = calculadora.calculatorPython12(5,7)
		self.assertEqual(resultado_suma, 12, "El test ha fallado")

if __name__ == '__main__':
    unittest.main()
