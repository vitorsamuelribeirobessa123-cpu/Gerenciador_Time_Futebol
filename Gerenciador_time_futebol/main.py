from treinador import Treinador
from jogador import Jogador
from partida import Partida
import csv

# São importadas as classes Treinador, Jogador e Partida, além do módulo csv.

lista_jogadores = []

# Lê os jogadores do arquivo CSV e cria objetos da classe Jogador.
with open("jogadores.csv", "r", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)

    for linha in leitor:
        jogador = Jogador(
            linha["nome"],
            int(linha["idade"]),
            float(linha["salario"]),
            int(linha["gols"]),
            linha["posicao"],
            linha["status"]
        )

        lista_jogadores.append(jogador)

# Exibe os nomes dos jogadores carregados do arquivo.
for jogador in lista_jogadores:
    print(jogador.get_nome())

print(" ")

# ==========================
# TREINADOR
# ==========================

treinador1 = Treinador("Carlo Ancelotti", 67, 5000000, 31)

treinador1.set_vitorias(10)

# Exibe as informações do treinador.
print("Nome:", treinador1.get_nome())
print("Idade:", treinador1.get_idade())
print("Anos de experiência:", treinador1.get_anos_experiencia())
print("Vitórias:", treinador1.get_vitorias())
print("Salário final:", treinador1.calcular_salario())


# ==========================
# JOGADORES
# ==========================

# Criação dos 25 jogadores da seleção.

jogador1 = Jogador("Alisson", 33, 5000000, 0, "Goleiro", "Titular")
jogador2 = Jogador("Ederson", 32, 4800000, 0, "Goleiro", "Reserva")
jogador3 = Jogador("Weverton", 38, 1200000, 0, "Goleiro", "Reserva")

jogador4 = Jogador("Marquinhos", 32, 4500000, 8, "Zagueiro", "Titular")
jogador5 = Jogador("Gabriel Magalhães", 28, 4200000, 12, "Zagueiro", "Titular")
jogador6 = Jogador("Bremer", 29, 3900000, 10, "Zagueiro", "Reserva")
jogador7 = Jogador("Léo Pereira", 30, 1800000, 15, "Zagueiro", "Reserva")

jogador8 = Jogador("Danilo", 35, 2500000, 12, "Lateral Direito", "Reserva")
jogador9 = Jogador("Wesley", 22, 1200000, 5, "Lateral Direito", "Titular")
jogador10 = Jogador("Alex Sandro", 35, 2300000, 10, "Lateral Esquerdo", "Reserva")
jogador11 = Jogador("Douglas Santos", 31, 2000000, 14, "Lateral Esquerdo", "Titular")

jogador12 = Jogador("Casemiro", 34, 5500000, 35, "Volante", "Titular")
jogador13 = Jogador("Bruno Guimarães", 28, 4200000, 22, "Volante", "Titular")
jogador14 = Jogador("Éderson", 27, 2500000, 15, "Volante", "Reserva")
jogador15 = Jogador("Fabinho", 32, 4500000, 28, "Volante", "Reserva")

jogador16 = Jogador("Lucas Paquetá", 28, 4000000, 40, "Meia", "Titular")
jogador17 = Jogador("Danilo", 25, 1800000, 10, "Meia", "Reserva")

jogador18 = Jogador("Vinícius Júnior", 26, 7000000, 45, "Atacante", "Titular")
jogador19 = Jogador("Rayan", 19, 3400000, 0, "Atacante", "Titular")
jogador20 = Jogador("Neymar", 34, 6000000, 80, "Atacante", "Reserva")
jogador21 = Jogador("Gabriel Martinelli", 25, 4000000, 22, "Atacante", "Reserva")
jogador22 = Jogador("Endrick", 19, 3500000, 18, "Atacante", "Reserva")
jogador23 = Jogador("Matheus Cunha", 27, 4200000, 35, "Centroavante", "Titular")
jogador24 = Jogador("Igor Thiago", 25, 2200000, 25, "Centroavante", "Reserva")
jogador25 = Jogador("Luiz Henrique", 25, 3000000, 30, "Atacante", "Reserva")

# Lista com todos os jogadores criados manualmente
lista_jogadores = [
    jogador1, jogador2, jogador3, jogador4, jogador5,
    jogador6, jogador7, jogador8, jogador9, jogador10,
    jogador11, jogador12, jogador13, jogador14, jogador15,
    jogador16, jogador17, jogador18, jogador19, jogador20,
    jogador21, jogador22, jogador23, jogador24, jogador25
]


# ==========================
# PARTIDA
# ==========================

# Cria uma partida contra a Argentina.
partida = Partida("Argentina")

# Define em quais minutos acontecerão os gols.
eventos_brasil = {
    17: jogador19,   # Rayan
    67: jogador23,   # Matheus Cunha
    88: jogador20    # Neymar 
}

eventos_adversario = [30, 82]   # Argentina faz gols aos 30 e 82 minutos

# Simula a partida utilizando os eventos definidos.
partida.simular_partida(eventos_brasil, eventos_adversario)



# ==========================
# ESTATÍSTICAS FINAIS
# ==========================

print("\n===== ESTATÍSTICAS DOS JOGADORES =====")

# Exibe as estatísticas do jogador Rayan.
print("\nJogador:")
print("Nome:", jogador19.get_nome())
print("Gols:", jogador19.get_gols())
print("Posição:", jogador19.get_posicao())
print("Status:", jogador19.get_status())
print("Salário Final:", jogador19.calcular_salario())

print()

# Exibe as estatísticas do jogador Matheus Cunha.
print("Jogador:")
print("Nome:", jogador23.get_nome())
print("Gols:", jogador23.get_gols())
print("Posição:", jogador23.get_posicao())
print("Status:", jogador23.get_status())
print("Salário Final:", jogador23.calcular_salario())


print()

# Exibe as estatísticas do jogador Neymar jr
print("Jogador:")
print("Nome:", jogador20.get_nome())
print("Gols:", jogador20.get_gols())
print("Posição:", jogador20.get_posicao())
print("Status:", jogador20.get_status())
print("Salário Final:", jogador20.calcular_salario())


with open("jogadores.csv", "w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo)

    escritor.writerow(["nome", "idade", "salario", "gols", "posicao", "status"])

    for jogador in lista_jogadores:
        escritor.writerow([
            jogador.get_nome(),
            jogador.get_idade(),
            jogador.get_salario(),
            jogador.get_gols(),
            jogador.get_posicao(),
            jogador.get_status()
        ])

print("\nDados dos jogadores salvos com sucesso!")
