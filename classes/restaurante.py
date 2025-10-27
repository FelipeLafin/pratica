from classes.pedidos import Pedido
from classes.cozinheiro import Cozinheiro
from utils.utils import Utils

class Restaurante:
    def __init__(self, qtd_cozinheiros, limite_pedidos):
        self.cozinheiros = [Cozinheiro() for _ in range(qtd_cozinheiros)]
        self.limite_pedidos = limite_pedidos
        self.normais = []
        self.prioritarios = []
        self.concluidos = 0
        self.recusados = 0
        
        self.total_normal = 0
        self.total_prioritario = 0
        self.total_geral = 0

        self.rejeitados_normal = 0
        self.rejeitados_prioritario = 0
        self.rejeitados_geral = 0

        self.concluidos_normal = 0
        self.concluidos_prioritario = 0
        self.concluidos_geral = 0

    def novo_pedido_normal(self, duracao):
        # Contabiliza o total de pedidos recebidos
        self.total_normal += 1
        self.total_geral += 1

        # Verifica se atingiu o limite de pedidos
        if len(self.normais) + len(self.prioritarios) >= self.limite_pedidos:
            # Contabiliza rejeição
            self.rejeitados_normal += 1
            self.rejeitados_geral += 1
            self.recusados += 1
        else:
            # Adiciona pedido normal na fila
            self.normais.append(Pedido(duracao))


    def novo_pedido_prioritario(self, duracao):
        # Contabiliza o total de pedidos recebidos
        self.total_prioritario += 1
        self.total_geral += 1

        # Verifica se o limite total foi atingido
        if len(self.normais) + len(self.prioritarios) >= self.limite_pedidos:
            # Contabiliza rejeição
            self.rejeitados_prioritario += 1
            self.rejeitados_geral += 1
            self.recusados += 1
        else:
            # Adiciona o pedido prioritário à fila
            self.prioritarios.append(Pedido(duracao, prioritario=True))


    def executar(self):
        # Atualiza cozinheiros (pedidos sendo concluídos)
        for cozinheiro in self.cozinheiros:
            pedido_concluido, finalizado = cozinheiro.trabalhar()

            if finalizado and pedido_concluido:
                if pedido_concluido.prioritario:
                    self.concluidos_prioritario += 1
                else:
                    self.concluidos_normal += 1

                self.concluidos_geral += 1
                self.concluidos += 1

        # Distribui pedidos para cozinheiros ociosos
        prioritarios_alocados = 0
        self.inicia_trabalho = True
        for cozinheiro in self.cozinheiros:
            if cozinheiro.esta_ocioso():
                # Até 2 prioritários por turno se houver ambos os tipos
                if self.prioritarios and self.normais and prioritarios_alocados < 2:
                    cozinheiro.atribuir_pedido(self.prioritarios.pop(0))
                    prioritarios_alocados += 1
                elif self.normais:
                    cozinheiro.atribuir_pedido(self.normais.pop(0))
                elif self.prioritarios:
                    cozinheiro.atribuir_pedido(self.prioritarios.pop(0))


    def status(self):
        fila_total = len(self.normais) + len(self.prioritarios)

        # Fila normal
        fila_normal = []
        for p in self.normais:
            fila_normal.append(p.duracao)
        print(f"   Fila normal: {fila_normal}")

        # Fila prioritária
        fila_prioritaria = []
        for p in self.prioritarios:
            fila_prioritaria.append(p.duracao)
        print(f"   Fila prioritária: {fila_prioritaria}\n")

        # Situação dos cozinheiros
        situacao = []
        for c in self.cozinheiros:
            situacao.append(c.tempo_restante())
        print(f"   Cozinheiros: {situacao}\n")

        # Informações gerais
        print(f"   Pedidos concluídos: {self.concluidos}")
        print(f"   Pedidos rejeitados: {self.recusados}\n")
        print(f"   Pedidos na fila: {fila_total}")
    
    def estatisticas(self):
        Utils.clear_screen()
        print("\n=== Estatísticas Finais ===\n")
        print("." + ("-" * 67) + ".")
        print(f"| {'':<22} | {'TOTAL':<10} | {'NORMAL':<12} | {'PRIORITÁRIO':<12} |")
        print("|" + ("-" * 24) + "|" + ("-" * 12) + "|" + ("-" * 14) + "|" + ("-" * 14) + "|")

        # Linhas da tabela principal
        print(f"| {'Pedidos recebidos':<22} | {self.total_geral:<10} | {self.total_normal:<12} | {self.total_prioritario:<12} |")
        print("|" + ("-" * 24) + "|" + ("-" * 12) + "|" + ("-" * 14) + "|" + ("-" * 14) + "|")
        print(f"| {'Pedidos rejeitados':<22} | {self.rejeitados_geral:<10} | {self.rejeitados_normal:<12} | {self.rejeitados_prioritario:<12} |")
        print("|" + ("-" * 24) + "|" + ("-" * 12) + "|" + ("-" * 14) + "|" + ("-" * 14) + "|")
        print(f"| {'Pedidos concluídos':<22} | {self.concluidos_geral:<10} | {self.concluidos_normal:<12} | {self.concluidos_prioritario:<12} |")
        print("|" + ("_" * 24) + "|" + ("_" * 12) + "|" + ("_" * 14) + "|" + ("_" * 14) + "|")


        print()
        print("." + ("-" * 67) + ".")
        print(f"| {'Cozinheiro':<15} | {'Tempo ocioso':<20} | {'Pedidos concluídos':<24} |")
        for c in self.cozinheiros:
            print("|" + ("-" * 17) + "|" + ("-" * 22) + "|" + ("-" * 26) + "|")
            print(f"| {c.pk:<15} | {c.tempo_ocioso:<20} | {c.concluidos:<24} |")
        print("|" + ("_" * 17) + "|" + ("_" * 22) + "|" + ("_" * 26) + "|")

        mais_ativo = None
        mais_concluidos = -1
        for c in self.cozinheiros:
            if c.concluidos > mais_concluidos:
                mais_concluidos = c.concluidos
                mais_ativo = c.pk

        # Exibir resultado
        print(f"\nCozinheiro que mais atendeu pedidos: {mais_ativo} ({mais_concluidos} pedidos)\n")