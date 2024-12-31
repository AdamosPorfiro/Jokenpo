class Jogadores:

    def __init__(self):
        self._Escolha_Computador = None
        self._Jogador = None
        self._contador_computador = 0
        self._contador_jogador = 0
        self.continuar = None

        
    def Escolhas(self):
        
        '''Bibliotecas usadas no app'''
        from random import choice

        '''Variaveis que somam os pontos da maquina e Jogador'''
        Opcoes = ['Pedra', 'Papel', 'Tesoura'] #Lista que será acessada para definir a escolha do computador

        '''
        Escolha da maquina e Jogador
        '''

        self._Escolha_Computador = choice(Opcoes) #Escolha aleatória do computador
        
        while True:
            self._Jogador = str(input('Escolha [ Pedra | Papel | Tesoura ]: ')).strip().title()
            match self._Jogador:
                case 'Pedra' | 'Papel' | 'Tesoura':
                    break
                case _:
                    print('Opção inválida! Digite novamente')
    
    def Exibir_inicio_jogo(self):
        
        '''
        O jogo se inicia e começa a verificação do vencedor
        '''

        from time import sleep
        print(
    '''
    ░░░░░██╗░█████╗░
    ░░░░░██║██╔══██╗
    ░░░░░██║██║░░██║
    ██╗░░██║██║░░██║
    ╚█████╔╝╚█████╔╝
    ░╚════╝░░╚════╝░''')
        
        sleep(1)
        print(
    '''
    ██╗░░██╗███████╗███╗░░██╗
    ██║░██╔╝██╔════╝████╗░██║
    █████═╝░█████╗░░██╔██╗██║
    ██╔═██╗░██╔══╝░░██║╚████║
    ██║░╚██╗███████╗██║░╚███║
    ░╚═╝░░╚═╝╚═════╝╚═╝░░╚══╝''')
        
        sleep(1)
        print(
    '''
    ██████╗░░█████╗░
    ██╔══██╗██╔══██╗
    ██████╔╝██║░░██║
    ██╔═══╝░██║░░██║
    ██║░░░░░╚█████╔╝
    ╚═╝░░░░░░╚════╝░\n''')

    def adicionar_pontos_jogador(self):
        self._contador_jogador += 1
    
    def adicionar_pontos_computador(self):
        self._contador_computador += 1

    def exibir_pontos(self):
        if self._contador_computador > self._contador_jogador:
            print('\nGAME OVER, você perdeu!!!')
            print(f'\nPontos jogador: {self._contador_jogador}\nPontos computador: {self._contador_computador}')

        if self._contador_computador == self._contador_jogador:
            print('\nGAME OVER, empatou!!!')
            print(f'Pontos jogador: {self._contador_jogador}\nPontos computador: {self._contador_computador}')

        if self._contador_computador < self._contador_jogador:
            print('\nGAME OVER, você venceu!!!')
            print(f'Pontos jogador: {self._contador_jogador}\nPontos computador: {self._contador_computador}')

    def Verificacao_do_vencedor(self):

        if self._Escolha_Computador == 'Pedra' and self._Jogador == 'Tesoura' or \
           self._Escolha_Computador == 'Papel' and self._Jogador == 'Pedra' or \
           self._Escolha_Computador == 'Tesoura' and self._Jogador == 'Papel':
            self.adicionar_pontos_computador()
            print(f"Computador escolheu: {self._Escolha_Computador}, você escolheu: {self._Jogador}")
            print("Você perdeu, essa partida!")

        elif self._Escolha_Computador == self._Jogador:
            print(f"Computador escolheu: {self._Escolha_Computador}, você escolheu: {self._Jogador}")
            print("Empatou, essa partida!")
            self.adicionar_pontos_computador()
            self.adicionar_pontos_jogador()

        else:
            print(f"Computador escolheu: {self._Escolha_Computador}, você escolheu: {self._Jogador}")
            print("Você venceu, a partida!")    
            self.adicionar_pontos_jogador()

    # def Continuar_aplicacao(self):
    #     while True:
    #         self.continuar = str(input('Deseja continuar o jogo [S/N]: ')).strip().upper()
    #         if self.continuar not in 'S' or 'N':
    #             continue
    #         else:
    #             break
