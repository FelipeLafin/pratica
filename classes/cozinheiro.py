class Cozinheiro:
    contador_pk = 1
    def __init__(self):
        self.pedido = None  # Nenhum pedido inicialmente
        self.tempo_ocioso = 0
        self.concluidos = 0
        self.pk = Cozinheiro.contador_pk
        Cozinheiro.contador_pk += 1
        
    def esta_ocioso(self):
        if self.pedido is None:
            self.tempo_ocioso += 1
        else:
            self.tempo_ocioso = 0
        return self.pedido is None

    def atribuir_pedido(self, pedido):
        self.pedido = pedido

    def trabalhar(self):
        if self.pedido:
            self.pedido.duracao -= 1
            if self.pedido.duracao <= 0:
                pedido_concluido = self.pedido
                self.pedido = None
                self.concluidos += 1
                return pedido_concluido, True  # Pedido finalizado
        return None, False  # Nenhum pedido finalizado


    def tempo_restante(self):
        return 0 if self.esta_ocioso() else self.pedido.duracao
