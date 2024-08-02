import os
import zipfile
import shutil
from extras import carregar_json, salvar_json, limpar_json, varificar_pasta_zips

def extrair():
    # Limpa as configurações do JSON
    limpar_json()

    # Carrega as configurações do JSON
    config = carregar_json()

    # Define o caminho do projeto atual
    caminho_projeto = os.getcwd()

    # Verifica se existe uma pasta chamada 'archive' e cria se não existir
    caminho_guardar_zips = varificar_pasta_zips(caminho_projeto)

    # Solicita o caminho do arquivo ZIP
    caminho_ficheiro_zip = input('Insira o caminho do arquivo ZIP (0 para atual): ').strip()

    # Verifica se o caminho do arquivo ZIP é válido
    while caminho_ficheiro_zip != '0' and not os.path.exists(caminho_ficheiro_zip):
        print('Caminho inválido. Tente novamente.')
        caminho_ficheiro_zip = input('Insira o caminho do arquivo ZIP (0 para atual): ').strip()

    # Se o caminho do arquivo ZIP for '0', define o caminho do arquivo ZIP como o caminho atual
    if caminho_ficheiro_zip == '0':
        caminho_ficheiro_zip = caminho_projeto
        print(f'Caminho do ficheiro será {caminho_ficheiro_zip}\n')

    # Solicita o nome do arquivo ZIP
    nome_ficheiro_zip = input('Insira o nome do arquivo ZIP: ').strip()

    # Verifica se o nome do arquivo ZIP termina com '.zip' e não está vazio
    while not nome_ficheiro_zip.endswith('.zip') or not nome_ficheiro_zip:
        print('Nome inválido. Tente novamente.')
        nome_ficheiro_zip = input('Insira o nome do arquivo ZIP: ').strip()

    # Remove a extensão '.zip' do nome do arquivo ZIP
    nome_ficheiro_zip_sem = nome_ficheiro_zip[:-4]

    # Define os caminhos absolutos para o arquivo ZIP, a pasta temporária de extração e a pasta final de extração
    caminho_absoluto_zip = os.path.join(caminho_ficheiro_zip, nome_ficheiro_zip)
    caminho_zip_extraido_temp = os.path.join(caminho_projeto, nome_ficheiro_zip_sem)
    caminho_zip_extraido_final = os.path.join(caminho_guardar_zips, nome_ficheiro_zip_sem)

    # Atualiza as configurações do JSON com os caminhos
    config['caminho_projeto'] = caminho_projeto
    config['caminho_pasta_zips'] = caminho_guardar_zips

    config['caminho_ficheiro_zip'] = caminho_ficheiro_zip
    config['nome_ficheiro_zip'] = nome_ficheiro_zip
    config['nome_ficheiro_zip_sem'] = nome_ficheiro_zip_sem
    config['caminho_absoluto_zip'] = caminho_absoluto_zip
    config['caminho_zip_extraido_temp'] = caminho_zip_extraido_temp
    config['caminho_zip_extraido_final'] = caminho_zip_extraido_final

    # Salva as configurações atualizadas no JSON
    salvar_json(config)

    try:
        # Extrai o arquivo ZIP para a pasta temporária
        with zipfile.ZipFile(caminho_absoluto_zip, 'r') as arquivo_zip:
            os.makedirs(caminho_zip_extraido_temp, exist_ok=True)
            arquivo_zip.extractall(caminho_zip_extraido_temp)
        print('Arquivo ZIP extraído com sucesso.\n')
    except zipfile.BadZipFile:
        print('Erro: O ficheiro não é um zip válido!')
        return

    try:
        # Verifica se a pasta final de extração já existe e remove-a se existir
        if os.path.exists(caminho_zip_extraido_final):
            shutil.rmtree(caminho_zip_extraido_final)

        # Move a pasta temporária para a pasta final de extração
        shutil.move(caminho_zip_extraido_temp, caminho_guardar_zips)
        print('Arquivo extraído e movido com sucesso.')
    except FileNotFoundError:
        raise FileNotFoundError('A pasta "archive" não foi encontrada.')
    except Exception as e:
        print(f'Erro inesperado: {e}')
        raise Exception(f'Erro inesperado: {e}')

    while True:
        # Solicita ao usuário se quer mover a pasta ou sair
        escolha = int(input('Deseja mover a pasta ou sair? (1 para mover, 0 para sair): '))

        # Verifica a opção escolhida
        if escolha == 1:
            # Solicita o novo caminho para a pasta
            novo_caminho = input('\nInsira o novo caminho para a pasta: ')

            # Move a pasta para o novo caminho
            shutil.move(caminho_guardar_zips, novo_caminho)
            print('Pasta movida com sucesso.\n')
            break
        elif escolha == 0:
            break
        else:
            print('Opção inválida. Tente novamente.\n')
