from novo_app import Jogadores
jogador = Jogadores()

def main():

   while True:
    jogador.Escolhas()
    jogador.Exibir_inicio_jogo()
    jogador.Verificacao_do_vencedor()

    continuar = str(input('Deseja continuar o jogo [S/N]: ')).strip().upper()
    if continuar != 'S':
        break
if __name__ == '__main__':
    main()