class Selecao:
    def __init__(self, nome_selecao):
        self.__nome_selecao = nome_selecao
        self.__jogadores = []

    @property
    def nome_selecao(self):
        return self.__nome_selecao
    
    @property
    def jogadores(self):
        return self.__jogadores
    
    def contratar(self,novo_membro):
        self.__jogadores.append(novo_membro)

    def demitir(self,membro):
        if membro in self.__jogadores:
            self.__jogadores.remove(membro)

    def colocar_jogador_titular(self,jogador_titular):
       jogador_titular.set_status("Titular") 

    def listar_jogadores(self):
        print("([=Lista de Membros=])")
        for membro in self.__jogadores:
            print(f"{membro.get_nome()}")

    def listar_comissao(self, gols, comissao):
        c = float(comissao)
        print("([=Comissão=])")
        for i in range(int(gols)):
            print(f"Gol número {i+1} = R${c} adicionados.")