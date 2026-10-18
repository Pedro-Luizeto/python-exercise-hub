from time import sleep

while True:
    print('=== SÉRIE DE EXERCÍCIOS DE PYTHON ===')
    sleep(1)
    print('')

    print('[1] - Exercício 01 - fácil')
    print('[2] - Exercício 02 - fácil')
    print('[3] - Exercício 03 - difícil')
    print('[4] - Exercício 04 - médio')
    print('[5] - SAIR')

    escolha = input('Escolha uma opção: ')

    match escolha:

        case '1':
            print('CARREGANDO EXERCÍCIO 01...')
            sleep(1)
            print('')
            print('=== EXERCÍCIO 01 ===')
            print('')
            print('Crie um código onde é solicitado para o usuário inserir dois valores: o ano atual, e o ano de nascimento. O sistema deve calcular quantos anos ele tem de acordo com essas informações e exibir no console')
            sleep(1)

        case '2':
            print('CARREGANDO EXERCÍCIO 02...')
            sleep(1)
            print('')
            print('=== EXERCÍCIO 02 ===')
            print('')
            print('Crie um código onde o usuário deve inserir dois números e exiba a soma, subtração, multiplicação e divisão deles.')
            sleep(1)


        case '3':
            print('CARREGANDO EXERCÍCIO 03...')
            sleep(1)
            print('')
            print('=== EXERCÍCIO 03 ===')
            print('')
            print('Crie um código onde o usuário deve digitar três notas escolares e calcular a média delas.')
            sleep(1)


        case '4':
            print('CARREGANDO EXERCÍCIO 04...')
            sleep(1)
            print('')
            print('=== EXERCÍCIO 04 ===')
            print('')
            print('Verificador de Nota Mínima: Crie um código que pergunte ao usuário qual foi sua nota em um teste. Defina uma nota mínima para aprovação (por exemplo, 6). Use uma estrutura if para verificar se a nota do usuário é maior ou igual à nota mínima. Se for, exiba a mensagem "Você atingiu a nota mínima!".')
            print('')
        case '5':
            print('Saindo do programa...')
            break   