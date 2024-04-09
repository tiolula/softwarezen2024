from unittest import TestCase
import src.calculadora_de_cambio as calc

class TestesDaCalculadoraDeCambio(TestCase):

    def teste_exemplo(self):
        valor = 0
        taxa = 3.37
        resultado_esperado = 0

        resultado_obtido = calc.converter(valor, taxa)

        self.assertEqual(resultado_obtido, resultado_esperado)