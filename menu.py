from extras import limpar_json
from func import extrair


def menu_principal():
    menu = int(input('1 -> Extrair\n2 -> Criar3 -> Outras configuracao \n0 -> Sair\n-> '))
    if menu == 1:
        extrair()
    elif menu == 2:
        pass
    elif menu == 0:
        exit(1)
    else:
        print('Opção inválida. Tente novamente.')
        menu_principal()


def outros_menus():
    menu = int(input('1 -> Limpar configurações\n0 -> Sair\n-> '))
    if menu == 1:
        limpar_json()
    elif menu == 0:
        exit(1)
    else:
        print('Opção inválida. Tente novamente.')
        outros_menus()