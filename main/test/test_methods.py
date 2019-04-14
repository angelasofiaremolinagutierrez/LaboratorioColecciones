import unittest
from custom_functions import just_methods


class TestMethods(unittest.TestCase):
    def test_promedio_method(self):

        lista = [30, 28, 26, 27, 24, 22, 29, 28, 27, 26, 28, 29]
        res = just_methods.calcular_promedio(lista)
        self.assertEqual(res, 27)

    def test_calcular_elemento_mayor_method(self):

        lista = [30, 28, 26, 27, 24, 22, 29, 28, 27, 26, 28, 29]
        res = just_methods.calcular_elemento_mayor(lista)
        self.assertEqual(res, 30)

    def test_calcular_desviacion_estandar_method(self):

        lista = [30, 28, 26, 27, 24, 22, 29, 28, 27, 26, 28, 29]
        res = just_methods.calcular_desviacion_estandar(lista)
        self.assertEqual(res, 2.256304299271065)
