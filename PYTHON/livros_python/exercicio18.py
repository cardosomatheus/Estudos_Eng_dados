""" 
8.12 Sanduíches: Crie uma função que aceite uma lista de itens que uma pessoa quer
em um sanduíche. A função deve ter um parâmetro que colete todos os itens
fornecidos na chamada de função e deve exibir um resumo do sanduíche que está
sendo solicitado. Chame a função três vezes, com um número diferente de argumentos
a cada vez.

8.13 Perfil de usuário: Comece com uma cópia do user_profile.py da página 194. Crie
um perfil de si mesmo chamando build_profile(), com seu primeiro nome e sobrenome
e três outros pares chave-valor que o representem.

8.14 Carros: Crie uma função que armazena informações sobre um carro em um
dicionário. A função deve sempre receber um fabricante e um nome de modelo. Em
seguida, deve aceitar um número arbitrário de argumentos nomeados. Chame a função
com as informações necessárias e dois outros pares nome-valor, como uma cor ou um
recurso opcional. Sua função deve funcionar mais ou menos assim:
car = make_car('subaru', 'outback', color='blue', tow_package=True)
Exiba o dicionário retornado para garantir que todas as informações foram
corretamente armazenadas.
"""

def sanduíche (*arg):
    print('lista de itens do sanduiche: ')
    for value in arg:
        print(f' - {value}')
        
sanduíche('tomate','salada','carne','carne dnv', 'mais carne', 'pao', 'ovo')
sanduíche('tomate','salada','carne','carne dnv', 'pao', 'ovo')
sanduíche('tomate','salada','carne', 'pao' )


def build_profile(first, last, **user_info):
    """Cria um dicionário contendo tudo o que sabemos sobre um usuário"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    
    return user_info

user_profile = build_profile('albert', 'einstein',location='princeton',
                             field='physics')
print(user_profile)

def make_car (fabricante, modelo, **kwargs):
    kwargs['fabricante'] = fabricante
    kwargs['modelo'] = modelo
    
    return kwargs


car = make_car(fabricante='honda', modelo='Honda Fit', ano=2003,km=150.00, 
               cor='preto')
    
print(car)