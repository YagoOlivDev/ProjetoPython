from time import sleep
print('\033[1;30m=-\033[m' * 40)
print('\033[1;38mOlá, me chamo Jasmine. Sou a IA de investimentos do banco Jupiter!')
nome = str(input('\033[1;38mQual é o seu nome senhor(a)? '))
print('\033[1;38mÉ um prazer telo(a) aqui senhor(a) {}.'.format(nome))
print('\033[1;30m=-\033[m' * 40)
while True:
    r = str(input('\033[1;38mSenhor(a) {} gostaria de fazer uma aplicação de investimentos conosco do banco Jupiter? '
                  .format(nome)).upper())

    if r == 'SIM' or r == 'CLARO' or r == 'QUERO SIM' or r == 'S':
        print('\033[1;38mOk, tenho duas opções de investimentos pro senhor(a)')
        print('\033[1;38mEscolha a baixo:')
        print('\033[1;30m=================================\033[m')
        print('\033[1;38m[ 1 ] Ações (Renda Variável)')
        print('\033[1;38m[ 2 ] Rendimento CDB (Renda Fixa)')
        print('\033[1;38m[ 3 ] Nenhum dos dois')
        print('\033[1;30m=================================\033[m')
        VxF = str(input('Digite uma opção: '))
        print('\033[1;30m=-\033[m' * 40)

        while VxF != '1' and VxF != '2' and VxF != '3':
            print('\033[1;38mOpção inválida!')
            print('\033[1;30m=================================\033[m')
            print('\033[1;38m[ 1 ] Ações (Renda Variável)')
            print('\033[1;38m[ 2 ] Rendimento CDB (Renda Fixa)')
            print('\033[1;38m[ 3 ] Nenhum dos dois')
            print('\033[1;30m=================================\033[m')
            VxF = str(input('Digite uma opção: '))
            print('\033[1;30m=-\033[m' * 40)

        if VxF == '1':
            print('\033[1;38mOk tenho senhor(a), tenho 2opções de ações disponiveis aqui no nosso banco')
            print('Escolha:')
            print('\033[1;30m==================================================\033[m')
            print('\033[1;38m[ 1 ] Ações Banco do Brasil, cada cota custa 38R$')
            print('\033[1;38m[ 2 ] Ações Petrobras, cada cota custa 30R$')
            print('\033[1;38m[ 3 ] Cancelar Investimentos')
            print('\033[1;30m==================================================\033[m')
            acoes = str(input('Qual ação o senhor(a) deseja comprar? '))

            while acoes != '1' and acoes != '2' and acoes != '3':
                print('\033[1;38mOpção inválida!')
                print('\033[1;30m=-\033[m' * 40)
                print('\033[1;38mEscolha:')
                print('\033[1;30m==================================================\033[m')
                print('\033[1;38m[ 1 ] Ações Banco do Brasil, cada cota custa 38R$')
                print('\033[1;38m[ 2 ] Ações Petrobras, cada cota custa 30R$')
                print('\033[1;38m[ 3 ] Cancelar Investimentos')
                print('\033[1;30m==================================================\033[m')
                acoes = str(input('Qual ação o senhor(a) deseja comprar? '))

            if acoes == '1':
                bb = 38
                qtd = 0
                valorinv = float(input('\033[1;38mQual valor deseja aplicar? '))

                while valorinv < bb:
                    print('\033[1;38mValor inválido!')
                    valorinv = float(input('Deseja aplicar quanto?'))

                if valorinv >= bb:
                    qtd = valorinv / bb
                    print(f'\033[1;38mSenhor(a) esse valor investido dá o total de {qtd:.0f} ações do Banco do Brasil.')
                    print('O senhor só precisa confirmar a compra de ações, a baixo:')
                    print('\033[1;30m=========================\033[m')
                    print('\033[1;38m[ 1 ] Confirmar compra!')
                    print('\033[1;38m[ 2 ] Cancelar compra!')
                    print('\033[1;30m=========================\033[m')
                    Cac = str(input('Digite sua opção: '))
                    print('\033[1;30m=========================\033[m')

                    while Cac != '1' and Cac != '2':
                        print('Opção inválida')
                        print('Tente novamente:')
                        print('\033[1;30m=========================\033[m')
                        print('\033[1;38m[ 1 ] Confirmar compra!')
                        print('\033[1;38m[ 2 ] Cancelar compra!')
                        print('\033[1;30m=========================\033[m')
                        Cac = str(input('Digite sua opção: '))
                        print('\033[1;30m=========================\033[m')

                    if Cac == '1':
                        print('\033[1;38mConfirmando...')
                        sleep(1.5)
                        print('Aguarde um instante...')
                        sleep(1.5)
                        print('Mais um pouco...')
                        sleep(1.5)
                        print('Finalizando...')
                        sleep(1.5)
                        print('\033[1;38mAplicação confirmada!')
                        print(f'\033[1;38mPronto senhor, você recebeu o total de {qtd:.0f} ações do Banco do Brasil em'
                              f' sua carteira digital!')
                        print('\033[1;38mAté a proxima!')
                        print('\033[1;30m=-\033[m' * 40)
                        exit()
                    elif Cac == 2:
                        print('\033[1;38mInvestimento cancelado!')
                        print('\033[1;38mAté a proxima!')
                        exit()

            elif acoes == '2':
                pt = 30
                qtd = 0
                valorinv =  float(input('\033[1;38mQual valor deseja aplicar? '))

                while valorinv < pt:
                    print('Valor inválido!')
                    valorinv = float(input('\033[1;38mDeseja aplicar quanto?'))

                if valorinv >= pt:
                    qtd = valorinv / pt
                    print(f'Senhor(a) esse valor investido dá o total de {qtd:.0f} ações da Petrobras.')
                    print('O senhor só precisa confirmar a compra de ações, a baixo:')
                    print('\033[1;30m=========================\033[m')
                    print('\033[1;38m[ 1 ] Confirmar compra!')
                    print('\033[1;38m[ 2 ] Cancelar compra!')
                    print('\033[1;30m=========================\033[m')
                    Cac = str(input('Digite sua opção: '))
                    print('\033[1;30m=========================\033[m')

                    while Cac != '1' and Cac != '2':
                        print('Opção inválida')
                        print('Tente novamente:')
                        print('\033[1;30m=========================\033[m')
                        print('\033[1;38m[ 1 ] Confirmar compra!')
                        print('\033[1;38m[ 2 ] Cancelar compra!')
                        print('\033[1;30m=========================\033[m')
                        Cac = str(input('Digite sua opção: '))
                        print('\033[1;30m=========================\033[m')

                    if Cac == '1':
                        print('\033[1;38mConfirmando...')
                        sleep(1.5)
                        print('Aguarde um instante...')
                        sleep(1.5)
                        print('Mais um pouco...')
                        sleep(1.5)
                        print('Finalizando...')
                        sleep(1.5)
                        print('\033[1;38mAplicação confirmada!')
                        print(
                            f'\033[1;38mPronto senhor, você recebeu o total de {qtd:.0f} ações da Petrobras'
                            f' em sua carteira digital!')
                        print('\033[1;38mAté a proxima!')
                        print('\033[1;30m=-\033[m' * 40)
                        exit()
                    elif Cac == '2':
                        print('\033[1;38mInvestimento cancelado!')
                        print('\033[1;38mAté a proxima!')
                        exit()

                    print('\033[1;30m=-\033[m' * 40)
                    exit()

            elif acoes == '3':
                print('\033[1;38mOk senhor(a), investimento cancelado, até a proxima!')
                break

        elif VxF == '2':
            print('\033[1;38mOk, escolha uma opção de investimento a baixo')
            print('\033[1;30m===============================================================================\033[m')
            print('\033[1;38mOpção [ 1 ] com rendimento de 2% ao mês, que você só irá poder sacar após 1ano.')
            print('\033[1;38mOpção [ 2 ] com rendimento de 1% ao mês, com liquidez diária.')
            print('\033[1;38mOpção [ 3 ] Cancelar investimentos.')
            print('\033[1;30m===============================================================================\033[m')
            opcao = str(input('\033[1;38mQual a sua escolha senhor(a)? '))

            while opcao != '1' and opcao != '2' and opcao != '3':
                print('\033[1;38mOpção invalida!')
                print('\033[1;30m===============================================================================\033[m')
                print('\033[1;38mOpção [ 1 ] com rendimento de 2% ao mês, que você só irá poder sacar após 1ano. ')
                print('\033[1;38mOpção [ 2 ] com rendimento de 1% ao mês, com liquidez diária. ')
                print('\033[1;38mOpção [ 3 ] Cancelar investimentos. ')
                print('\033[1;30m===============================================================================\033[m')
                opcao = str(input('\033[1;38mQual a sua escolha senhor(a)? '))

            if opcao == '1':
                v = float(input('\033[1;38mQual o valor que o senhor(a) quer investir? R$'))
                rend = (v * 24/100) + v
                print('\033[1;38mSeu rendimento anual será de R${} com a opção 1'.format(rend))
                print('\033[1;30m=-\033[m' * 40)

                while True :
                    aplicacao = str(input('\033[1;38mPodemos prosseguir com a aplicação? ').upper())
                    if aplicacao == 'SIM' or aplicacao == 'CLARO' or aplicacao == 'QUERO SIM' or aplicacao == "S":
                        print('\033[1;38mOk, você só precisa confirmar a aplicação a baixo:')
                        print('\033[1;30m==============================\033[m')
                        print('\033[1;38m[ 1 ] "Confirmar aplicação" ')
                        print('\033[1;38m[ 2 ] "Recusar aplicação" ')
                        print('\033[1;30m==============================\033[m')
                        ca = str(input('Digite sua opção: '))
                        print('\033[1;30m==============================\033[m')

                        while ca != '1' and ca != '2':
                            print('\033[1;38mOpção invalida!')
                            print('\033[1;38mTente Novamente!')
                            print('\033[1;30m==============================\033[m')
                            print('\033[1;38m[ 1 ] "Confirmar aplicação" ')
                            print('\033[1;38m[ 2 ] "Recusar aplicação" ')
                            print('\033[1;30m==============================\033[m')
                            ca = str(input('\033[1;38mDigite sua opção: '))
                            print('\033[1;30m==============================\033[m')

                        if ca == '1':
                            print('\033[1;38mConfirmando...')
                            sleep(1.5)
                            print('Aguarde um instante...')
                            sleep(1.5)
                            print('Mais um pouco...')
                            sleep(1.5)
                            print('Finalizando...')
                            sleep(1.5)
                            print('\033[1;38mAplicação confirmada!')
                            print('\033[1;38mPronto senhor(a) {}, lembre que o senhor(a) só poderá sacar esse valor após um ano'.format(nome))
                            print('\033[1;38mPois escolheu a opção de maior rendimento e menor liquidez.')
                            print('\033[1;30m=-\033[m' * 40)
                            exit()

                        elif ca == 2:
                            print('\033[1;38mAplicação recusada!')
                            print('\033[1;38mIrei retornar esse processo ao inicio.')
                            break

                    elif aplicacao == 'NAO' or aplicacao == 'N' or aplicacao == 'QUERO NAO':
                        print('\033[1;38mNão? Irei retornar do inicio senhor(a)')
                        break

                    elif aplicacao != 'SIM' or aplicacao != 'CLARO' or aplicacao != 'S' or aplicacao != 'NAO' or aplicacao != 'N' or aplicacao != 'QUERO SIM' or aplicacao != 'QUERO NAO':
                        print('\033[1;38mNão entendi, vou perguntar novamente.')

            elif opcao == '2':
                v = float(input('\033[1;38mQual o valor que o senhor(a) quer investir? R$'))
                rend = (v * 12/100) + v
                print('\033[1;38mSeu rendimento anual será de R${} com a opção 2'.format(rend))
                print('\033[1;30m=-\033[m' * 40)

                while True:
                    aplicacao = str(input('\033[1;38mPodemos prosseguir com a aplicação?').upper())
                    if aplicacao == 'SIM' or aplicacao == 'CLARO' or aplicacao == 'QUERO SIM' or aplicacao == 'S':
                        print('\033[1;38mOk, você só precisa confirmar a aplicação a baixo:')
                        print('\033[1;30m==============================\033[m')
                        print('\033[1;38m[ 1 ] "Confirmar aplicação" ')
                        print('\033[1;38m[ 2 ] "Recusar aplicação "')
                        print('\033[1;30m==============================\033[m')
                        ca = str(input('Digite sua opção: '))
                        print('\033[1;30m==============================\033[m')

                        while ca != '1' and ca != '2':
                            print('\033[1;30m=-\033[m' * 40)
                            print('\033[1;38mOpção inválida!')
                            print('\033[1;38mTente novamente:')
                            print('\033[1;30m==============================\033[m')
                            print('\033[1;38m[ 1 ] "Confirmar aplicação" ')
                            print('\033[1;38m[ 2 ] "Recusar aplicação "')
                            print('\033[1;30m==============================\033[m')
                            ca = str(input('\033[1;38mDigite sua opção: '))
                            print('\033[1;30m==============================\033[m')

                        if ca == '1':
                            print('\033[1;38mConfirmando...')
                            sleep(1.5)
                            print('Agurde um instante...')
                            sleep(1.5)
                            print('Mais um pouco...')
                            sleep(1.5)
                            print('Finalizando...')
                            sleep(1.5)
                            print('\033[1;38mAplicação confirmada!')
                            print('\033[1;38mPronto senhor(a) {}, lembre que o senhor(a) só poderá sacar esse valor após um ano'
                                  .format(nome))
                            print('\033[1;30m=-\033[m' * 40)
                            exit()

                        elif ca == '2':
                            print('\033[1;38mAplicação recusada!')
                            print('\033[1;38mIrei retornar esse processo ao inicio.')
                            break

                    elif aplicacao == 'NAO' or aplicacao == 'N' or aplicacao == 'QUERO NAO':
                        print('\033[1;38mNão? Irei retornar do inicio senhor(a)')
                        break

                    elif aplicacao != 'SIM' or aplicacao != 'CLARO' or aplicacao != 'S' or aplicacao != 'NAO' or aplicacao !=  'N' or aplicacao != 'QUERO SIM' or aplicacao != 'QUERO NAO':
                        print('\033[1;38mNão entendi, vou perguntar novamente.')

            elif opcao == '3':
                print('\033[1;38mInvestimento Cancelado Com Sucesso!!')

        elif VxF == '3':
            print('\033[1;38mOk senhor(a), infelizmente só temos essas 2 opções de investimentos!')
            print('\033[1;38mEstamos trabalhando em novas opções, até a proxima!')
            break

    elif r == 'NAO' or r == 'N' or r == 'QUERO NAO':
        print('\033[1;38mOk, tenha um otimo dia!')
        break

    else:
        print('\033[1;30m=-\033[m' * 40)
        print('\033[1;38mNão entendi, irei refazer a pergunta')

print('\033[1;30m=-\033[m' * 40)