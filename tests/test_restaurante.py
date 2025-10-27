import unittest
from classes.restaurante import Restaurante

class TestRestaurante(unittest.TestCase):
    #Testes da classe Restaurante

    def setUp(self):
        self.restaurante = Restaurante(qtd_cozinheiros=2, limite_pedidos=3)

    def test_adicionar_pedido_normal(self):
        #Verifica se pedidos normais são adicionados corretamente
        self.restaurante.novo_pedido_normal(5)
        self.assertEqual(len(self.restaurante.normais), 1)
        self.assertEqual(self.restaurante.total_normal, 1)

    def test_adicionar_pedido_prioritario(self):
        #Verifica se pedidos prioritários são adicionados corretamente
        self.restaurante.novo_pedido_prioritario(3)
        self.assertEqual(len(self.restaurante.prioritarios), 1)
        self.assertEqual(self.restaurante.total_prioritario, 1)

    def test_rejeicao_de_pedidos(self):
        #Verifica se pedidos são rejeitados ao ultrapassar o limite
        for _ in range(4):
            self.restaurante.novo_pedido_normal(2)
        self.assertEqual(self.restaurante.recusados, 1)
        self.assertEqual(self.restaurante.rejeitados_geral, 1)

    def test_execucao_e_conclusao(self):
        #Testa a execução do restaurante e a conclusão de pedidos
        self.restaurante.novo_pedido_normal(1)
        self.restaurante.executar()
        self.restaurante.executar()
        self.assertEqual(self.restaurante.concluidos, 1)
