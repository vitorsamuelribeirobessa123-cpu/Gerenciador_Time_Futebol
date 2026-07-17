from membro import Membro

class Jogador(Membro):

    def __init__(self, nome, idade, salario, gols, posicao, status):
        """
        Inicializa um jogador com seus dados básicos.

        Parâmetros:
            nome (str): nome do jogador.
            idade (int): idade do jogador.
            salario (float): salário base do jogador.
            gols (int): quantidade de gols marcados.
            posicao (str): posição em que joga.
            status (str): situação do jogador no time.
        """
        super().__init__(nome, idade, salario)

        self.__gols = gols
        self.__posicao = posicao
        self.__status = status

    def get_gols(self):
        """
        Retorna a quantidade de gols do jogador.

        Retorna:
            int: quantidade de gols.
        """
        return self.__gols

    def get_posicao(self):
        """
        Retorna a posição do jogador.
        """
        return self.__posicao

    def get_status(self):
        """
        Retorna o status do jogador.

        Retorna:
         status do jogador.
        """
        return self.__status

    def set_gols(self, gols):
        """
        Altera a quantidade de gols do jogador.

        Parâmetros:
            gols: nova quantidade de gols.
        """
        self.__gols = gols

    def set_posicao(self, posicao):
        """
        Altera a posição do jogador.

        Parâmetros:
            posicao : nova posição do jogador.
        """
        self.__posicao = posicao

    def set_status(self, status):
        """
        Altera o status do jogador.

        Parâmetros:
            status: novo status do jogador.
        """
        self.__status = status

    def marcar_gol(self):
        """
        Incrementa em 1 a quantidade de gols do jogador.

        Retorna:
            None.
        """
        self.__gols += 1

    def calcular_salario(self):
        """
        Calcula o salário final do jogador.

        O cálculo considera o salário base acrescido
        de um bônus por gol marcado.

        Retorna:
         salário final do jogador.
        """
        bonus_por_gol = 500
        return self.get_salario() + (self.__gols * bonus_por_gol)