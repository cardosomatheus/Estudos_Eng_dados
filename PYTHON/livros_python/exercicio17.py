"""
8.6 Nome de cidades: Escreva uma função chamada city_country() que recebe o nome
de uma cidade e seu país. A função deve retornar uma string formatada como esta:
"Santiago, Chile"
Chame sua função com pelo menos três pares cidade-país e exiba os valores
retornados.

8.7 Álbum: Escreva uma função chamada make_album() que crie um dicionário
representando um álbum de música. A função deve ter o nome de um artista e o título
de álbum, e deve retornar um dicionário com essas duas informações. Utilize a função
para criar três dicionários representando álbuns distintos. Exiba cada valor de retorno
para mostrar que os dicionários estão armazenando adequadamente as informações do
álbum.
Use None para adicionar um parâmetro opcional ao make_album() que possibilite
armazenar o número de músicas em um álbum. Se a linha chamadora incluir um valor
para o número de músicas, adicione esse valor ao dicionário do álbum. Crie, pelo
menos, uma nova chamada de função que inclua o número de músicas em um álbum.

8.8 Álbuns de usuários: Comece com seu programa do Exercício 8.7. Escreva um loop
while que possibilite aos usuários inserir o artista e o título de um álbum. Após receber
essas informações, chame make_album() com a entrada do usuário e exiba o dicionário
criado. Não se esqueça de incluir um valor de saída no loop while.
"""

def city_country(city, country):
    return f'{city}, {country}'.title()

print(city_country(city='Belo Horizonte',country='Brasil'))
print(city_country(city='são paulo',country='Brasil'))
print(city_country(city='curitiba',country='Brasil'))


def make_album(artista, album, qtd_musica=None) :
    my_dict = {}
    artista1 = {
        'cantor': artista,
        'album': album,
        'musicas': qtd_musica
    }
    my_dict[artista] = artista1

    return my_dict

print(make_album('michael jackson' , 'Thriller'))
print(make_album('michael jackson' , 'Bad'))
print(make_album('michael jackson' , 'Dangerous ', 10))

condicional = True
while condicional:
    
    artista = str(input('Artista: '))
    album   = str(input('Album: '))
    musicas = int(input('Qts musicas do album: '))
    
    make_album(artista=artista,album=album, qtd_musica=musicas)
    
    quer_sair = str(input('Digite "Q" para sair: ')).upper() 
    if quer_sair == 'Q':
        condicional = False
    
    
    
def many_parameter(*values):
    """ 
        você consegue passar varios valores na variavel "VALUES" dessa forma, assim sendo todos se tornaram um unica tupla.
    """
    print(values)
    

many_parameter('jose','marcos','1','2','3','oooo)')


def build_profile(first, last, **user_info):
    """Cria um dicionário contendo tudo o que sabemos sobre um usuário"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',location='princeton',field='physics')
print(user_profile)