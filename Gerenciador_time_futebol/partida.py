import time

class Partida:

    def __init__(self, adversario):
        self.__adversario = adversario
        self.__placar_time = 0
        self.__placar_adversario = 0

    def simular_partida(self, eventos):

        print(f"\n⚽ Início da partida!")
        print(f"Brasil x {self.__adversario}\n")

        for minuto in range(1, 91):

            print(f"{minuto}'")

            if minuto in eventos:
                jogador = eventos[minuto]

                jogador.marcar_gol()
                self.__placar_time += 1

                print(f"⚽ GOL DO BRASIL!")
                print(f"Autor: {jogador.get_nome()}")
                print(f"Placar: Brasil {self.__placar_time} x {self.__placar_adversario} {self.__adversario}")

            time.sleep(0.5)

        print("\n🔔 Fim de jogo!")
        print(f"Placar Final: Brasil {self.__placar_time} x {self.__placar_adversario} {self.__adversario}")