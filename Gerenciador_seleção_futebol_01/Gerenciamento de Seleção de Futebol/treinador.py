from membro import Membro

class Treinador(Membro):

    def __init__(self, nome, idade, salario, anos_experiencia,):
        """
        Inicializa um treinador com seus dados básicos.

        Parâmetros:
            nome (str): nome do treinador.
            idade (int): idade do treinador.
            salario_base (float): salário base do treinador.
            anos_experiencia (int): anos de experiência.
        """
        super().__init__(nome, idade, salario)

        self.__anos_experiencia = anos_experiencia
        self.__vitorias = 0

    def get_anos_experiencia(self):
        """
        Retorna os anos de experiência do treinador.

        Retorna:
            int: anos de experiência.
        """
        return self.__anos_experiencia

    def set_anos_experiencia(self, anos_experiencia):
        """
        Altera os anos de experiência do treinador.

        Parâmetros:
            anos_experiencia (int): nova quantidade de anos.
        """
        self.__anos_experiencia = anos_experiencia

    def get_vitorias(self):
        """
        Retorna a quantidade de vitórias do treinador.

        Retorna:
            int: quantidade de vitórias.
        """
        return self.__vitorias

    def set_vitorias(self, vitorias):
        """
        Altera a quantidade de vitórias do treinador.

        Parâmetros:
            vitorias (int): nova quantidade de vitórias.
        """
        self.__vitorias = vitorias

    def registrar_vitoria(self):
        """
        Adiciona uma vitória ao treinador.

        Retorna:
            None.
        """
        self.__vitorias += 1

    def calcular_salario(self):
        """
        Calcula o salário final do treinador.

        O cálculo considera o salário base acrescido
        de um bônus por vitória.

        Retorna:
            float: salário final do treinador.
        """
        bonus_por_vitoria = 1000
        return self.get_salario() + (self.__vitorias * bonus_por_vitoria)