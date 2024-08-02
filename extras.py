import os
from json import loads, dumps, JSONDecodeError


def carregar_json():
    '''
    This function loads the content of the 'data/config.json' file as a dictionary.
    It uses the 'open' function to open the file in read mode with the 'utf-8' encoding.
    The 'loads' function from the 'json' module is used to parse the JSON data.
    
    Parameters:
    None
    
    Returns:
    A dictionary containing the data from the 'data/config.json' file.
    
    Raises:
    FileNotFoundError: If the file 'data/config.json' is not found.
    JSONDecodeError: If the file 'data/config.json' is not a valid JSON.
    Exception: If an unexpected error occurs while loading the file.
    '''

    try:
        # Open the 'data/config.json' file in read mode with the 'utf-8' encoding
        with open('data/config.json', 'r', encoding='utf-8') as arquivo:

            # Read the content of the file and parse it as a JSON
            return loads(arquivo.read())

    except FileNotFoundError as e:
        # If the file is not found, raise a FileNotFoundError with a custom message
        raise FileNotFoundError('Arquivo "config.json" não encontrado.') from e

    except JSONDecodeError as e:
        # If the file is not a valid JSON, raise a JSONDecodeError with a custom message
        raise JSONDecodeError('O arquivo "config.json" não é um JSON válido.') from e # type: ignore

    except Exception as e:
        # If an unexpected error occurs, raise an Exception with a custom message
        raise Exception(f'Ocorreu um erro inesperado: {e}') from e


def salvar_json(dados):
    '''
    This function saves the given dictionary as a JSON to the 'data/config.json' file.

    Parameters:
    dados (dict): The dictionary to be saved as a JSON.

    Returns:
    None

    Raises:
    FileNotFoundError: If the file 'data/config.json' is not found.
    TypeError: If the 'dados' parameter is not a dictionary.
    Exception: If an unexpected error occurs while saving the file.
    '''

    # Check if the parameter passed is a dictionary
    if not isinstance(dados, dict):
        # If it's not a dictionary, raise a TypeError with a custom error message
        raise TypeError('The "dados" parameter must be a dictionary.')

    try:
        # Open the 'data/config.json' file in write mode with the 'utf-8' encoding
        with open('data/config.json', 'w', encoding='utf-8') as arquivo:

            # Convert the dictionary to a JSON string using the dumps function from the json module
            # The indent parameter is set to 4 to make the JSON string more readable
            json_string = dumps(dados, indent=4)

            # Write the JSON string to the file
            arquivo.write(json_string)

    except FileNotFoundError as e:
        # If the file is not found, raise a FileNotFoundError with a custom message
        raise FileNotFoundError('Arquivo "config.json" não encontrado.') from e

    except Exception as e:
        # If an unexpected error occurs, raise an Exception with a custom message
        # The error message includes the original exception message
        raise Exception(f'Ocorreu um erro inesperado: {e}') from e


def limpar_json():
    '''
    This function clears the values of certain keys in the 'data/config.json' file.
    It loads the JSON data into a dictionary, modifies the dictionary, and then saves the modified dictionary back to the file.
    
    Parameters:
    None
    
    Returns:
    None
    '''

    # Load the JSON data from the 'data/config.json' file into a dictionary
    config = carregar_json()

    # Get the values of the keys 'caminho_projeto', 'caminho_pasta_zips', 'caminho_ficheiro_zip', 'nome_ficheiro_zip', 'nome_ficheiro_zip_sem',
    # 'caminho_absoluto_zip', 'caminho_zip_extraido_temp', and 'caminho_zip_extraido_final' from the dictionary
    caminho_projeto = config['caminho_projeto']
    caminho_pasta_zips = config['caminho_pasta_zips']
    caminho_ficheiro_zip = config['caminho_ficheiro_zip']
    nome_ficheiro_zip = config['nome_ficheiro_zip']
    nome_ficheiro_zip_sem = config['nome_ficheiro_zip_sem']
    caminho_absoluto_zip = config['caminho_absoluto_zip']
    caminho_zip_extraido_temp = config['caminho_zip_extraido_temp']
    caminho_zip_extraido_final = config['caminho_zip_extraido_final']

    # If the value of 'caminho_projeto' is not None, set its value to None in the dictionary
    if caminho_projeto is not None:
        config['caminho_projeto'] = None

    # If the value of 'caminho_pasta_zips' is not None, set its value to None in the dictionary
    if caminho_pasta_zips is not None:
        config['caminho_pasta_zips'] = None

    # If the value of 'caminho_ficheiro_zip' is not None, set its value to None in the dictionary
    if caminho_ficheiro_zip is not None:
        config['caminho_ficheiro_zip'] = None

    # If the value of 'nome_ficheiro_zip' is not None, set its value to None in the dictionary
    if nome_ficheiro_zip is not None:
        config['nome_ficheiro_zip'] = None

    # If the value of 'nome_ficheiro_zip_sem' is not None, set its value to None in the dictionary
    if nome_ficheiro_zip_sem is not None:
        config['nome_ficheiro_zip_sem'] = None

    # If the value of 'caminho_absoluto_zip' is not None, set its value to None in the dictionary
    if caminho_absoluto_zip is not None:
        config['caminho_absoluto_zip'] = None

    # If the value of 'caminho_zip_extraido_temp' is not None, set its value to None in the dictionary
    if caminho_zip_extraido_temp is not None:
        config['caminho_zip_extraido_temp'] = None

    # If the value of 'caminho_zip_extraido_final' is not None, set its value to None in the dictionary
    if caminho_zip_extraido_final is not None:
        config['caminho_zip_extraido_final'] = None

    # Save the modified dictionary back to the 'data/config.json' file
    salvar_json(config)


def varificar_pasta_zips(caminho_projeto):
    '''
    This function checks if a folder named 'archive' exists in the given project path.
    If the folder does not exist, it creates the folder.
    
    Parameters:
    caminho_projeto (str): The path of the project.
    
    Returns:
    str: The path of the 'archive' folder.
    '''

    # Concatenate the project path and the name of the folder 'archive'
    # We are joining the project path and the name of the folder 'archive' together
    # This will create a new path that combines the project path and the folder name
    # The function os.path.join() is used to safely join paths
    # This is necessary because different operating systems have different conventions for how paths should be separated
    # For example, in Windows, the path separator is '\' while in Unix-based systems it is '/'
    caminho_guardar_zips = os.path.join(caminho_projeto, 'archive')

    # Check if the folder 'archive' exists
    # We are using the os.path.exists() function to check if the folder exists
    # This function returns True if the path exists and False if it does not exist
    if not os.path.exists(caminho_guardar_zips):
        # If the folder does not exist, create the folder
        # We are using the os.makedirs() function to create the folder
        # This function creates a new directory and any necessary parent directories if they do not already exist
        # The function will raise an exception if the directory cannot be created
        os.makedirs(caminho_guardar_zips)

    # Return the path of the 'archive' folder
    # We are returning the path of the 'archive' folder that was created or already exists
    return caminho_guardar_zips
