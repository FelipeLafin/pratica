import unittest
from classes.restaurante import Restaurante

class TestEstatisticas(unittest.TestCase):
    #Testa o cálculo e exibição das estatísticas do restaurante

    def setUp(self):
        self.r = Restaurante(qtd_cozinheiros=2, limite_pedidos=5)
        # Simula pedidos concluídos manualmente
        self.r.cozinheiros[0].concluidos = 5
        self.r.cozinheiros[1].concluidos = 3
        self.r.cozinheiros[0].tempo_ocioso = 2
        self.r.cozinheiros[1].tempo_ocioso = 4

    def test_mais_produtivo(self):
        #Verifica se identifica corretamente o cozinheiro mais produtivo
        mais_ativo = None
        mais_concluidos = -1
        for c in self.r.cozinheiros:
            if c.concluidos > mais_concluidos:
                mais_concluidos = c.concluidos
                mais_ativo = c.pk
            self.assertIsNotNone(mais_ativo)
            self.assertEqual(mais_concluidos, 5)


    def test_soma_concluidos_total(self):
        #Verifica se o total de concluídos é a soma dos cozinheiros
        total = sum(c.concluidos for c in self.r.cozinheiros)
        self.assertEqual(total, 8)