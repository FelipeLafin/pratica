import unittest
from classes.pedidos import Pedido

class TestPedido(unittest.TestCase):
    def test_criacao_pedido_normal(self):
        #Verifica se o pedido normal é criado corretamente
        p = Pedido(duracao=5)
        self.assertEqual(p.duracao, 5)
        self.assertFalse(p.prioritario)

    def test_criacao_pedido_prioritario(self):
        #Verifica se o pedido prioritário é criado corretamente
        p = Pedido(duracao=3, prioritario=True)
        self.assertEqual(p.duracao, 3)
        self.assertTrue(p.prioritario)

if __name__ == '__main__':
    unittest.main()
