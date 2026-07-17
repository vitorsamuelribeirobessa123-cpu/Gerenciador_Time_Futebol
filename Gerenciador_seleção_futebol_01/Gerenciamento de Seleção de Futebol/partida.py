import time

class Partida:

    def __init__(self, selecao_casa, adversario):
        self.__selecao_casa = selecao_casa
        self.__adversario = adversario
        self.__placar = '0 x 0'
        self.__resultado ='Ainda vai realizar'

    def iniciar_partida(self, eventos, gols_casa, gols_adversario):
        print('\nDIA DE CLÁSSICO NO MINEIRÃO: BRASIL E ARGENTINA!')
        time.sleep(1.0)
        print()
        print('As duas seleções se enfrentam pela Taça do Copa do Mundo!🏆')
        print()
        time.sleep(3.0)

        print('\n ESCALAÇÃO BRASIL')
        print("=" * 45)
        print("Treinador: Carlo Ancelotti")
        print("-" * 45)
        print('Jogadores:')
        print(" - Alisson (Goleiro)")
        print(" - Danilo (Lateral Direito)")
        print(" - Marquinhos (Zagueiro)")
        print(" - Gabriel Magalhães (Zagueiro)")
        print(" - Douglas Santos (Lateral Esquerdo)")
        print(" - Casemiro (Volante)")
        print(" - Bruno Guimarães (Volante)")
        print(" - Neymar Jr (Meia)")
        print(" - Raian (Atacante)")
        print(" - Vinícius Júnior (Atacante)")
        print(" - Matheus Cunha (Centroavante)")

        time.sleep(3.0) 
        print()

        print('\n ESCALAÇÃO ARGENTINA')
        print("=" * 45)
        print(' Treinador: Lionel Scaloni')
        print("-" * 45)
        print("Jogadores:")
        print(" - Emiliano Martínez (Goleiro)")
        print(" - Nahuel Molina (Lateral Direito)")
        print(" - Cristian Romero (Zagueiro)")
        print(" - Nicolás Otamendi (Zagueiro)")
        print(" - Nicolás Tagliafico (Lateral Esquerdo)")
        print(" - Rodrigo De Paul (Volante)")
        print(" - Enzo Fernández (Volante)")
        print(" - Alexis Mac Allister (Meia)")
        print(" - Ángel Di María (Atacante)")
        print(" - Lautaro Martínez (Centroavante)")
        print(" - Lionel Messi (Atacante)")

        time.sleep(3.0) 
        print()

        print('Aaapitou o juiz! Coooomeça o jogo!')
        time.sleep(2.0)
        print()

        for minuto in eventos:
            jogador = eventos[minuto]
            jogador.marcar_gol()

            if jogador in self.__selecao_casa.jogadores:
                print(f"[{minuto}'] GOOOOOOOOL DOOOOO BRASIIIIIL!!!")
            else:
                print(f"[{minuto}'] GOOOOOL DA ARGENTINAAA!!!")

            print(f'Sabe de queeeem?: {jogador.get_nome()}\n')
            time.sleep(1.0)

        print('Com 5 minutos de acréscimo o jogo está chegando ao fim! 2 para o Brasil e 1 para a Argentina.' )
        time.sleep(1.0)
        print()

        print('FIIIM DE JOGOO! Apita o árbitro encerrando esse superclássico emocionante com vitória da Seleção Brasileira!\n')
        time.sleep(1.0)

        self.registrar_resultado(gols_casa, gols_adversario)


    def registrar_resultado(self, gols_casa, gols_adversario):
        self.__placar = f"{gols_casa} x {gols_adversario}"

        if gols_casa > gols_adversario:
            self.__resultado = 'VITÓRIA DO BRASIL!'

            for membro in self.__selecao_casa.jogadores:
                if type(membro).__name__ == "Treinador":
                    membro.registrar_vitoria()

        elif gols_adversario > gols_casa:
            self.__resultado = 'VITÓRIA DA ARGENTINA!'
            
            for membro in self.__adversario.jogadores:
                if type(membro).__name__ == "Treinador":
                    membro.registrar_vitoria()
        else:
            self.__resultado = "EMPATE!"

        print(f"Placar Final: {self.__placar}")
        print(f"Resultado: {self.__resultado}")
        print()