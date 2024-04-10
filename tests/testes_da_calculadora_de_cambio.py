from unittest import TestCase
import src.calculadora_de_cambio as calc

# Desafio
# - Dado um valor e uma taxa de câmbio, a conversão seja feita
# - A calculadora deve fazer os cálculos e retornar o valor com duas casas decimais
# - Caso o resultado tenha mais de 2 casas decimais, ele deve ser arredondado para baixo (truncado)
# - Imposto é fixo em 1.1% (IOF)

# Carlos Hung

class TestesDaCalculadoraDeCambio(TestCase):

    def teste_valor_0_taxa_3_37_imposto_0_0011_resultado_esperado_0 (self):

        # Arrange

        valor = 0
        taxa = 3.37
        imposto = 0.0011
        resultado_esperado = 0

        # Act

        resultado_obtido = calc.converter(valor, taxa, imposto)

        # Assert

        self.assertEqual(resultado_obtido, resultado_esperado)

    def teste_valor_1_taxa_3_37_imposto_0_0011_resultado_esperado_3_37 (self):

        # Arrange

        valor = 1
        taxa = 3.37
        imposto = 0.0011
        resultado_esperado = 3.37

        # Act

        resultado_obtido = calc.converter(valor, taxa, imposto)

        # Assert

        self.assertEqual(resultado_obtido, resultado_esperado)

    def teste_valor_10_taxa_3_37_imposto_0_0011_resultado_esperado_33_71 (self):

        # Arrange

        valor = 10
        taxa = 3.37
        imposto = 0.0011
        resultado_esperado = 33.71

        # Act

        resultado_obtido = calc.converter(valor, taxa, imposto)

        # Assert

        self.assertEqual(resultado_obtido, resultado_esperado)