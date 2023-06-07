from random import randint
from time import sleep


# Funções e Regras/Functions and Rules
def par_ou_impar():
    print('\033[7;34m==*== Par ou Ímpar! ==*==\033[m')
    while True:
        jogador = (input('\033[1;34mDigite um número: \033[m'))
        if jogador.isnumeric():
            jogador = int(jogador)
            break
        else:
            print('ERROR <Number not found>! Digite um número inteiro.')
    # O pc irá escolher um número inteiro aleatório entre 0 e 10.
    # The computer will choose a random integer number between 0 and 10.
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ''
    # Verificicar se o input é uma das opções, caso contrário ele irá se repetir.
    # Check if the input is one of the options, otherwise it will repeat.
    while tipo not in ('P', 'I'):
        tipo = input('\033[31mPar\033[m ou \033[32mÍmpar\033[m? '
                     '[Digite \033[31mP\033[m ou \033[32mI\033[m] ').strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}.', end=' ')
    if total % 2 == 0:
        resultado = 'P'
        print('Deu PAR!')
    else:
        resultado = 'I'
        print('Deu ÍMPAR!')
    if tipo == resultado:
        print('Você VENCEU! 🏅🏅🏅')
        return True
    else:
        print('Você PERDEU! Não desista, tente jogar outra vez.')
        return False


# Menu Principal/Main Menu
def main():
    nome = input('Qual é o seu nome? ').strip().capitalize()
    print('Bem-Vindo(a) ao jogo!')
    sleep(0.50)
    for p in range(3, -1, -1):
        if p == 0:
            p = 'começar'
        print(f'{p}...')
        sleep(0.25)
    # Contador de 'vitórias', 'derrotas' e de 'partidas jogadas'.
    # Counter for 'wins', 'losses', and 'played matches'.
    vitorias = 0
    derrotas = 0
    partidas = 0
    while True:
        print('-' * 30)
        print(f'{"MENU PRINCIPAL":^30}')
        print('-' * 30)
        print('1 - Jogar Par ou Ímpar')
        print('2 - Sair do jogo')
        opcao = input('Sua opção: ')
        if opcao == '1':
            if par_ou_impar():
                vitorias += 1
            else:
                derrotas += 1
                partidas = vitorias + derrotas
        elif opcao == '2':
            if partidas == 0:
                print('Saindo do jogo...')
                sleep(1)
                break
            else:
                print('*' * 30)
                print(f'Obrigado por jogar, {nome}! Você venceu {vitorias} vez(es). \n '
                      f'E houve um total de {derrotas} derrota(s) nas {partidas} partida(s) que você jogou.')
                print('Volte mais vezes!')
                print('*' * 30)
            break
        else:
            print('Opção inválida. Tente novamente.')
        sleep(1)


if __name__ == '__main__':
    main()
