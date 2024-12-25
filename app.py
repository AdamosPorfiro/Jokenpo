'''
Jokempô

Pedra, Papel ou Tesoura.

Regras do jogo:
================================
Pedra ganha da Tesoura;
Pedra perde para Papel;

Papel ganha da Pedra;
Papel perde para tesoura;

Tesoura ganha de Papel;
Tesoura perde para Pedra;
================================
'''

'''
Jogada escolhida pela máquina
'''
from random import choice
from time import sleep
Ponto_Jogador = 0
Ponto_Computador = 0

Opcoes = ['Pedra', 'Papel', 'Tesoura']
Escolha_Computador = choice(Opcoes)

'''
Escolha do jogador
'''
resp_1 = 'S'
while resp_1 == 'S':
    resp = 'S'
    while resp == 'S':
        Jogador = str(input('Escolha [ Pedra | Papel | Tesoura ]: ')).strip().title()
        # if Jogador in {'Pedra', 'Papel', 'Tesoura'}:
        #     resp = 'N'
        # else:
        #     resp = 'S'
        match Jogador:
            case 'Pedra' | 'Papel' | 'Tesoura':
                resp = 'N'
            case _:
                print('Opção inválida! Digite novamente')
                resp = 'S'

    '''
    O jogo se inicia e começa a verificação do vencedor
    '''

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

    '''
    Verifica quem é o vencedor e marca o ponto
    '''

    if Escolha_Computador in 'Pedra' and Jogador in 'Tesoura':
        print(f'Computador: {Escolha_Computador} vs Jogador: {Jogador}','Você Perdeu!', sep='\n')
        Ponto_Computador += 1

    elif Escolha_Computador in 'Papel' and Jogador in 'Pedra':
        print(f'Computador: {Escolha_Computador} vs Jogador: {Jogador}','Você Perdeu!', sep='\n')
        Ponto_Computador += 1

    elif Escolha_Computador in 'Tesoura' and Jogador in 'Papel':
        print(f'Computador: {Escolha_Computador} vs Jogador: {Jogador}','Você Perdeu!', sep='\n')
        Ponto_Computador += 1

    elif Escolha_Computador in 'Pedra' and Jogador in 'Pedra':
        print(f'Computador: {Escolha_Computador} vs Jogador: {Jogador}','Empate!', sep='\n')
        Ponto_Computador += 1
        Ponto_Jogador += 1

    elif Escolha_Computador in 'Papel' and Jogador in 'Papel':
        print(f'Computador: {Escolha_Computador} vs Jogador: {Jogador}','Empate!', sep='\n')
        Ponto_Computador += 1
        Ponto_Jogador += 1

    elif Escolha_Computador in 'Tesoura' and Jogador in 'Tesoura':
        print(f'Computador: {Escolha_Computador} vs Jogador: {Jogador}','Empate!', sep='\n')
        Ponto_Computador += 1
        Ponto_Jogador += 1

    else:
        print(f'Computador: {Escolha_Computador} vs Jogador: {Jogador}','Você Venceu!', sep='\n')
        Ponto_Jogador += 1

    print(f'\nPontos jogador: {Ponto_Jogador}\nPontos Computador: {Ponto_Computador}')

    resp_2 = 'Erro'
    while resp_2 == 'Erro':
        resp_1 = str(input('Deseja continuar [S/N]: ')).strip().upper()
        match resp_1:
            case 'S':
                resp_1 = 'S'
                resp_2 = 'Cont'
            case 'N':
                resp_1 = 'N'
                resp_2 = 'Fim'

if Ponto_Computador > Ponto_Jogador:
    print('\nGame Over! Você perdeu o jogo.')
elif Ponto_Computador == Ponto_Jogador:
    print('\nGame Over! O jogo empatou.')
else:
    print('\nGame Over! Parabens, você venceu o jogo.')

print('Muito obrigado por jogar, volte sempre!')