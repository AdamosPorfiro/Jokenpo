
class Jogadores:

    def __init__(self):
        self._Escolha_Computador = None
        self._Jogador = None
        self._contador_computador = None
        self._contador_jogador = None

        
    def Escolhas(self):
        
        '''Bibliotecas usadas no app'''
        from random import choice

        '''Variaveis que somam os pontos da maquina e Jogador'''
        Opcoes = ['Pedra', 'Papel', 'Tesoura'] #Lista que será acessada para definir a escolha do computador

        '''
        Escolha da maquina e Jogador
        '''

        self._Escolha_Computador = choice(Opcoes) #Escolha aleatória do computador
        
        resp = 'S'
        while resp == 'S':
            self._Jogador = str(input('Escolha [ Pedra | Papel | Tesoura ]: ')).strip().title()
            # if self._Jogador in {'Pedra', 'Papel', 'Tesoura'}:
            #     resp = 'N'
            # else:
            #     resp = 'S'
            match self._Jogador:
                case 'Pedra' | 'Papel' | 'Tesoura':
                    resp = 'N'
                case _:
                    print('Opção inválida! Digite novamente')
                    resp = 'S'
    
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

    def Verificacao_do_vencedor(self):         
        Ponto_Jogador = 0
        Ponto_Computador = 0

        '''
        Verifica quem é o vencedor e marca o ponto
        '''

        if self._Escolha_Computador in 'Pedra' and self._Jogador in 'Tesoura':
            print(f'Computador: {self._Escolha_Computador} vs self._Jogador: {self._Jogador}','Você Perdeu!', sep='\n')
            Ponto_Computador += 1

        elif self._Escolha_Computador in 'Papel' and self._Jogador in 'Pedra':
            print(f'Computador: {self._Escolha_Computador} vs Jogador: {self._Jogador}','Você Perdeu!', sep='\n')
            Ponto_Computador += 1

        elif self._Escolha_Computador in 'Tesoura' and self._Jogador in 'Papel':
            print(f'Computador: {self._Escolha_Computador} vs Jogador: {self._Jogador}','Você Perdeu!', sep='\n')
            Ponto_Computador += 1

        elif self._Escolha_Computador in 'Pedra' and self._Jogador in 'Pedra':
            print(f'Computador: {self._Escolha_Computador} vs Jogador: {self._Jogador}','Empate!', sep='\n')
            Ponto_Computador += 1
            Ponto_Jogador += 1

        elif self._Escolha_Computador in 'Papel' and self._Jogador in 'Papel':
            print(f'Computador: {self._Escolha_Computador} vs Jogador: {self._Jogador}','Empate!', sep='\n')
            Ponto_Computador += 1
            Ponto_Jogador += 1

        elif self._Escolha_Computador in 'Tesoura' and self._Jogador in 'Tesoura':
            print(f'Computador: {self._Escolha_Computador} vs Jogador: {self._Jogador}','Empate!', sep='\n')
            Ponto_Computador += 1
            Ponto_Jogador += 1

        else:
            print(f'Computador: {self._Escolha_Computador} vs Jogador: {self._Jogador}','Você Venceu!', sep='\n')
            Ponto_Jogador += 1

        print(f'\nPontos Jogador: {Ponto_Jogador}\nPontos Computador: {Ponto_Computador}')
