import time
'''Importa-se a função time.'''

class Partida:

    def __init__(self, adversario):
        '''O adversário é instanciado e o placar começa em 0.'''
        self.__adversario = adversario
        self.__placar_time = 0
        self.__placar_adversario = 0

    def get_adversario(self):
        return self.__adversario

    def simular_partida(self, eventos_brasil, eventos_adversario):
        print(f"\n⚽ Início da partida!")
        print(f"Brasil x {self.get_adversario()}\n")

        for minuto in range(1, 91):
            '''O minuto é exibido de 1 até 90.'''
            print(f"{minuto}'")

            # Gol do Brasil
            if minuto in eventos_brasil:
                jogador = eventos_brasil[minuto]

                jogador.marcar_gol()
                self.__placar_time += 1

                print(f"⚽ GOL DO BRASIL!")
                print(f"Autor: {jogador.get_nome()}")
                print(f"Placar: Brasil {self.__placar_time} x {self.__placar_adversario} {self.get_adversario()}")

            # Gol do adversário
            if minuto in eventos_adversario:
                self.__placar_adversario += 1

                print(f"⚽ GOL DA {self.get_adversario()}!")
                print(f"Placar: Brasil {self.__placar_time} x {self.__placar_adversario} {self.get_adversario()}")

            time.sleep(0.3)

        print("\n🔔 Fim de jogo!")
        print(f"Placar Final: Brasil {self.__placar_time} x {self.__placar_adversario} {self.get_adversario()}")
