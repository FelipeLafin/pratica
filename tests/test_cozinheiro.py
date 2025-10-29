import unittest
from classes.cozinheiro import Cozinheiro
from classes.pedidos import Pedido

class TestCozinheiro(unittest.TestCase):
    def setUp(self):
        self.cozinheiro = Cozinheiro()

    def test_cozinheiro_inicialmente_ocioso(self):
        #Verifica se o cozinheiro começa sem pedido
        self.assertTrue(self.cozinheiro.esta_ocioso())

    def test_atribuir_pedido(self):
        #Verifica se o cozinheiro recebe um pedido
        pedido = Pedido(duracao=4)
        self.cozinheiro.atribuir_pedido(pedido)
        self.assertFalse(self.cozinheiro.esta_ocioso())

    def test_trabalhar(self):
        #Simula o trabalho até a conclusão de um pedido
        pedido = Pedido(duracao=1)
        self.cozinheiro.atribuir_pedido(pedido)
        _, finalizado = self.cozinheiro.trabalhar()
        self.assertTrue(finalizado)
        self.assertEqual(self.cozinheiro.concluidos, 1)
        self.assertTrue(self.cozinheiro.esta_ocioso())

if __name__ == '__main__':
    unittest.main()