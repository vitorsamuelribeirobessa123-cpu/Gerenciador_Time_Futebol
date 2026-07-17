from treinador import Treinador
from jogador import Jogador
from partida import Partida
from selecao import Selecao
import csv

# SELEÇÕES
brasil = Selecao('Brasil')
argentina = Selecao('Argentina')

# TREINADOR 
treinador1 = Treinador('Carlo Ancelotti', 67, 5000000, 31)

# Treinador criado manualmente
treinador1 = Treinador(
    "Carlo Ancelotti",
    67,
    5000000,
    31
)

treinador1.set_vitorias(10)

treinador1.set_vitorias(treinador1.get_vitorias() + 1)
brasil.contratar(treinador1)

# JOGADORES BRASIL
jogador1 = Jogador("Alisson", 33, 5000000, 0, "Goleiro", "Titular")
jogador2 = Jogador("Ederson", 32, 3600000, 0, "Goleiro", "Reserva")
jogador3 = Jogador("Weverton", 38, 900000, 0, "Goleiro", "Reserva")

jogador4 = Jogador("Marquinhos", 32, 7000000, 0, "Zagueiro", "Titular")
jogador5 = Jogador("Gabriel Magalhães", 28, 4000000, 1, "Zagueiro", "Titular")
jogador6 = Jogador("Bremer", 29, 3000000, 0, "Zagueiro", "Reserva")
jogador7 = Jogador("Léo Pereira", 30, 800000, 0, "Zagueiro", "Reserva")

jogador8 = Jogador("Danilo", 34, 6000000, 0, "Lateral Direito", "Reserva")
jogador9 = Jogador("Wesley", 22, 1200000, 0, "Lateral Direito", "Titular")
jogador10 = Jogador("Alex Sandro", 35, 1500000, 2, "Lateral Esquerdo", "Reserva")
jogador11 = Jogador("Douglas Santos", 32, 6000000, 0, "Lateral Esquerdo", "Titular")

jogador12 = Jogador("Casemiro", 34, 9400000, 2, "Volante", "Titular")
jogador13 = Jogador("Bruno Guimarães", 28, 50000000, 0, "Volante", "Titular")
jogador14 = Jogador("Éderson", 27, 4000000, 0, "Volante", "Reserva")
jogador15 = Jogador("Fabinho", 32, 6000000, 0, "Volante", "Reserva")

jogador16 = Jogador("Lucas Paquetá", 28, 4000000, 4, "Meia", "Titular")
jogador17 = Jogador("Danilo", 24, 700000, 0, "Meia", "Reserva")

jogador18 = Jogador("Vinícius Júnior", 25, 12000000, 9, "Atacante", "Titular")
jogador19 = Jogador("Rayan", 20, 3400000, 0, "Atacante", "Titular")
jogador20 = Jogador("Neymar", 34, 6000000, 80, "Atacante", "Titular")
jogador21 = Jogador("Gabriel Martinelli", 25, 4000000, 3, "Atacante", "Reserva")
jogador22 = Jogador("Endrick", 19, 3500000, 2, "Atacante", "Reserva")
jogador23 = Jogador("Matheus Cunha", 27, 2500000, 35, "Centroavante", "Titular")
jogador24 = Jogador("Igor Thiago", 25, 2200000, 25, "Centroavante", "Reserva")
jogador25 = Jogador("Luiz Henrique", 25, 2000000, 30, "Atacante", "Reserva")


# Lista com todos os jogadores criados manualmente
lista_jogadores = [
    jogador1, jogador2, jogador3, jogador4, jogador5,
    jogador6, jogador7, jogador8, jogador9, jogador10,
    jogador11, jogador12, jogador13, jogador14, jogador15,
    jogador16, jogador17, jogador18, jogador19, jogador20,
    jogador21, jogador22, jogador23, jogador24, jogador25
]

brasil.contratar(jogador20)
brasil.contratar(jogador18)

messi = Jogador("Lionel Messi", 39, 110000000, 121, "Atacante", "Titular")
argentina.contratar(messi)


partida = Partida(brasil, argentina)

eventos = {
    4: jogador20,
    41: jogador18,
    82: messi

}

salario_sem_bonus_neymar = jogador20.calcular_salario()
salario_sem_bonus_vini = jogador18.calcular_salario()
salario_sem_bonus_treinador = treinador1.calcular_salario()

# salario_sem_bonus_messi = messi.calcular_salario()
# salario_sem_bonus_treinador_arg = treinador_arg.calcular_salario()

partida.iniciar_partida(eventos, 2, 1)

print("\n===== ESTATÍSTICAS E SALÁRIOS =====")

print('Treinador:')
print('Nome:', treinador1.get_nome())
print('Idade:', treinador1.get_idade())
print('Anos de experiência:', treinador1.get_anos_experiencia())
print('Vitórias:', treinador1.get_vitorias())
print('Salário (sem bônus): R$', salario_sem_bonus_treinador)
print('Salário (com bônus): R$', treinador1.calcular_salario())

print( )

print('Jogador:')
print('Nome:', jogador20.get_nome())
print('Gols:', jogador20.get_gols())
print('Posição:', jogador20.get_posicao())
print('Status:', jogador20.get_status())
print('Salário (sem bônus): R$', salario_sem_bonus_neymar)
print('Salário (com bônus): R$', jogador20.calcular_salario())

print( )

print('Jogador:')
print('Nome:', jogador18.get_nome())
print('Gols:', jogador18.get_gols())
print('Posição:', jogador18.get_posicao())
print('Status:', jogador18.get_status())
print('Salário (sem bônus): R$', salario_sem_bonus_vini)
print('Salário (com bônus): R$', jogador18.calcular_salario())

print( )

# print('Treinador Argentina:')
# print('Nome:', treinador_arg.get_nome())
# print('Idade:', treinador_arg.get_idade())
# print('Anos de experiência:', treinador_arg.get_anos_experiencia())
# print('Vitórias:', treinador_arg.get_vitorias())
# print('Salário (sem bônus): R$', salario_sem_bonus_treinador_arg) 
# print('Salário (com bônus): R$', treinador_arg.calcular_salario())

#print()

# print('Jogador Argentina:')
# print('Nome:', messi.get_nome())
# print('Gols:', messi.get_gols())
# print('Posição:', messi.get_posicao())
# print('Status:', messi.get_status())
# print('Salário (sem bônus): R$', salario_sem_bonus_messi) 
# print('Salário (com bônus): R$', messi.calcular_salario())
#print()


# Salvar os jogadores e o treinador no arquivo CSV
with open("jogadores.csv", "w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo)

    escritor.writerow([
        "nome", "idade", "salario", "gols", "posicao", "status"
    ])

    for jogador in lista_jogadores:
        escritor.writerow([
        jogador.get_nome(),
        jogador.get_idade(),
        jogador.calcular_salario(),
        jogador.get_gols(),
        jogador.get_posicao(),
        jogador.get_status()
    ])

print("Jogadores salvos com sucesso!")




with open("treinador.csv", "w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo)

    escritor.writerow([
        "nome", "idade", "salario", "anos_experiencia", "vitorias"
    ])

    escritor.writerow([
    treinador1.get_nome(),
    treinador1.get_idade(),
    treinador1.calcular_salario(),
    treinador1.get_anos_experiencia(),
    treinador1.get_vitorias()
])


print("Treinador salvo com sucesso!")

"""
novo_jogador = Jogador("Hugo Souza", 24, 3000000, 1, "Goleiro", "Reserva") 
print(f"Novo jogador contratado:{novo_jogador.get_nome()}" )
brasil.contratar(novo_jogador)

brasil.coclocar_jogador_titular(novo_jogador)
print(f"Novo status do {novo_jogador.get_nome()}:{novo_jogador.set_status}" )

brasil.demitir(novo_jogador)
print("Demitir: {novo_jogador.get_nome()}")
"""
