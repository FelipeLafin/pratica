import os
from classes.restaurante import Restaurante

class Programa:
    def main(self):
        qtd_cozinheiros = int(input("Digite a quantidade de cozinheiros (>0): "))
        limite_pedidos = int(input("Digite o limite da fila de pedidos (>0): "))
        r = Restaurante(qtd_cozinheiros, limite_pedidos)

        while True:
            acao = input("\nAção [N=normal, P=prioritário, E=executar, S=sair]: ").lower()

            if acao == "n":
                duracao = int(input("Duração do pedido normal: "))
                r.novo_pedido_normal(duracao)
            elif acao == "p":
                duracao = int(input("Duração do pedido prioritário: "))
                r.novo_pedido_prioritario(duracao)
            elif acao == "e":
                r.executar()
            elif acao == "s":
                r.relatorio()
                print("Encerrando o sistema...")
                break
            else:
                print("Opção inválida!")
            os.system('cls' if os.name == 'nt' else 'clear')
            r.status()

if __name__ == '__main__':
    programa = Programa()
    programa.main()
