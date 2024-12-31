from novo_app import Jogadores

def main():
    jogador = Jogadores()
    while True:
        
        jogador.Escolhas()
        jogador.Exibir_inicio_jogo()
        jogador.Verificacao_do_vencedor()
        
        continuar = str(input('Deseja continuar o jogo [S/N]: ')).strip().upper()
        while True:
            if continuar == 'S':
                break
            elif continuar == 'N':
                print('\nJogo finalizado, obrigado por jogar [VOLTE SEMPRE!]')
                jogador.exibir_pontos()
                break
        if continuar == 'N':
            break
        
if __name__ == '__main__':
    main()