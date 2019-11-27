def jogo():
    print('Bem vindos ao jogo de 21')
    quant_jogadores = int(input('Quantas pessoas irão jogar? '))
    jogadores = []
    i = 0
    while i < quant_jogadores:
        jogadores.append(input('Nome do Jogador: '))
        i += 1


jogo()


def baralho():
    baralho = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
    baralho *= 4
    return baralho

baralho()

