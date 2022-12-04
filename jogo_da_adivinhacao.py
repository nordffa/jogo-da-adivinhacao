from random import randint

numero_sorteado, tentativas = randint(0, 10), 0
nome = str(input('Qual o seu nome? ')).capitalize().strip()
print(f'Olá {nome}, seja bem-vindo ao jogo da adivinhação!')
while True:
    tentativas += 1
    jogada = int(input('Escolha um número entre 0 e 10: '))
    if jogada == numero_sorteado:
        print(f'Parabéns! Você acertou em {tentativas} tentativa(s)!')
        break
    else:
        if jogada < numero_sorteado:
            print(f'Maior do que {jogada}...')
        else:
            print(f'Menor do que {jogada}...')
