"""
10.11 Número favorito: Desenvolva um programa que solicite o número favorito do
usuário. Use json.dumps() para armazenar esse número em um arquivo. Escreva um
programa separado que leia esse valor e exiba a mensagem: “Eu sei o seu número
favorito! É _____”.

10.12 Relembrando o número favorito: Combine os dois programas que escreveu no
Exercício 10.11 em um arquivo. Se o número já estiver armazenado, informe o número
favorito ao usuário. Caso contrário, solicite o número favorito do usuário e armazene-o
em um arquivo. Execute o programa duas vezes para verificar se funciona.

10.13 Dicionário do usuário: O exemplo remember_me.py armazena apenas uma
informação, o nome de usuário. Incremente esse exemplo solicitando mais duas
informações sobre o usuário e armazene todas as informações coletadas em um
dicionário. Escreva esse dicionário em um arquivo com json.dumps(), e o releia usando
json.loads(). Exiba um resumo mostrando exatamente o que seu programa relembra
sobre o usuário.

10.14 Verificando usuário: A listagem final de remember_me.py pressupõe que o
usuário já forneceu seu nome de usuário ou que o programa está sendo executado
pela primeira vez. Devemos modificá-lo, caso o usuário atual não seja a pessoa que
usou o programa pela última vez.
Antes de exibir uma mensagem de boas-vindas em greet_user(), pergunte ao usuário
se o seu nome está correto.
"""
from pathlib import Path
import json

def salva_numero_favorito():
    number = int(input('numero favorito: '))
    path = Path('favorite_number.json')
    contents = json.dumps(number)
    path.write_text(contents)


def busca_numero_favorito():
    path  = Path('favorite_number.json')
    contents = path.read_text()
    numero_favorito = json.loads(contents)
    print(f'Eu sei o seu número favorito! É {numero_favorito}.')
        

def identifica_numero_favorito():    
    path  = Path('favorite_number.json')
    if path.exists():
        busca_numero_favorito()
    else:           
        salva_numero_favorito()
        busca_numero_favorito()



def identifica_usuarios():
    path = Path('all_users.json')
    
    if path.exists():
        busca_usuarios(path=path)
    else:
        salva_usurios(path=path)
        busca_usuarios(path=path)
    
    
def escreve_usuario_json():
    """ Cria usuarios e aidiona no dict final para ser criado um .json"""
    all_user = dict()
    
    ind_usuario = True
    while ind_usuario:
        user_dict  = dict()
        username = input("What is your name? ")
        last_name = input("What is your last name? ")
        age = input("What is your age? ")
        
        # Cria o dict do usuario.
        user_dict['username']  = username
        user_dict['last_name'] = last_name
        user_dict['age']       = age 
        all_user[username] = user_dict

        # Chave para sair do loop
        sair = input('Quser sair? escreva Q: ').upper().strip()
        if sair == 'Q':
            ind_usuario = False
    
    return all_user


def salva_usurios(path):
    """ Salva os usuarios deinidos em um .json"""
    all_user = escreve_usuario_json()
    
    contents =  json.dumps(all_user)
    path.write_text(contents)


def busca_usuarios(path):
    """ Busca os usuarios no file.json e lista um por um. """
    contents = path.read_text()
    users = json.loads(contents)

    print('USERS: \n')
    for user, user_data in users.items():
        print(f'{user}: {user_data}')



identifica_usuarios()
identifica_numero_favorito()        
