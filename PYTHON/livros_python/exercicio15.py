"""
6.1 Pessoa: Use um dicionário para armazenar informações sobre uma pessoa que você
conhece. Armazene o nome, sobrenome, idade e a cidade onde mora. Nomeie as
chaves como first_name, last_name, age e city. Exiba cada informação armazenada em
seu dicionário.

6.2 Números favoritos: Use um dicionário para armazenar os números favoritos das
pessoas. Pense em cinco nomes e os utilize como chaves em seu dicionário. Pense em
um número favorito para cada pessoa e armazene cada um como um valor em seu
dicionário. Exiba o nome de cada pessoa e seu número favorito. Para que tudo fique
ainda mais divertido, pergunte a alguns amigos e obtenha alguns dados reais para o
seu programa.

"""
pessoa = {
    'first_name': 'Matheus',
    'last_name': 'Cardoso',
    'age': 24,
    'city': 'Belo Horizonte'
}

# Exibindo as informações
print(f"Nome: {pessoa.get('first_name',None)}")
print(f"Sobrenome: {pessoa.get('last_name',None)}")
print(f"Idade: {pessoa.get('age',None)}")
print(f"Cidade: {pessoa.get('city',None)}")

numeros = {'jose': 10,
           'marcus': 5,
           'matheus': 8,
           'ana': 1,
           'lucia': 2}

for key, value in numeros.items():
    print(f'o valor favorito de {key} é {value}. \n')