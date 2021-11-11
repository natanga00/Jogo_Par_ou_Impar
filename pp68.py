from random import randint
v = 0
while True:
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('PAR ou ÍMPAR ? ')).strip().upper()[0]
        print('=' * 51)
    jogador = int(input('Jogue um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    print(f'Você jogou {jogador} e o computador jogou {computador}! O total é {total}!')
    if tipo == 'P':
        if total % 2 == 0:
            print('Parabéns, você ganhou !!!')
            v += 1
        else:
            print('Sinto muito, você perdeu !!!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Parabéns, você ganhou !!!')
            v += 1
        else:
            print('Sinto muito, você perdeu !!!')
            break
print(f'FIM DO JOGO ! Você venceu {v} vez(es) !')