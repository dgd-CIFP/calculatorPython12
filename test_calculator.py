import unittest
import calculadora

class TestCalculator(unittest.TestCase):
	def test_calculator12(self):
		resultado_multiplicacion = calculadora.calculatorPython12(5,7)
		self.assertEqual(resultado_multiplicacion, 35, "El test ha fallado")

if __name__ == '__main__':
    unittest.main()
