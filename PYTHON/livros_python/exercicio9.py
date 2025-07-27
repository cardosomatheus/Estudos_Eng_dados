"""
3.8 Conhecendo o mundo: Pense em pelo menos cinco lugares do mundo que você
gostaria de conhecer.
    • Armazene esses locais em uma lista. Verifique se ela não está em ordem alfabética.
    • Exiba sua lista na ordem original. Não se preocupe em exibir a lista ordenadamente;
    basta exibi-la como uma lista crua do Python.
    • Use sorted() para exibir sua lista em ordem alfabética, sem alterar a lista original.
    • Mostre que sua lista ainda está na ordem original exibindo-a.
    • Use o sorted() para exibir sua lista em ordem alfabética reversa, sem alterar a ordem
    original dela.
    • Demonstre que sua lista ainda está na ordem original exibindo-a mais uma vez.
    • Use o reverse() para alterar a ordem de sua lista. Exiba essa lista para mostrar que
    sua ordem foi alterada.
    • Use o reverse() para alterar a ordem de sua lista novamente. Exiba-a a fim de
    mostrar que voltou à ordem original.
    • Use o sort() para alterar sua lista para que ela seja armazenada em ordem
    alfabética. Exiba a lista para mostrar que sua ordem foi alterada.
    • Use sort() para alterar sua lista, de modo que ela seja armazenada em ordem
    alfabética inversa. Exiba a lista para mostrar que sua ordem foi alterada.
    3.9 Convidados para o jantar: Recorra a um dos programas dos exercícios 3.4 a 3.7
    (páginas 75-76), e use len() para exibir uma mensagem indicando o número de
    pessoas que você está convidando para jantar.
    3.10 Funções: Pense em coisas que você conseguiria armazenar em uma lista. Por
    exemplo, você pode criar uma lista de montanhas, rios, países, cidades, idiomas, ou
    qualquer outra coisa que quiser. Crie um programa com uma lista contendo esses itens
"""

viagens = ['islandia', 'noruega','estonia', 'coreia do sul', 'romenia']
sorted_viagens = sorted(viagens)

# Armazene esses locais em uma lista. Verifique se ela não está em ordem alfabética.
for posicao in range(0,len(viagens)):
    if viagens[posicao] != sorted_viagens[posicao]:
        print(f'As lista estão direntes. \n{viagens[posicao]} e {sorted_viagens[posicao]}')
        break

    print('Lista ordenadas.')


# Exiba sua lista na ordem original. Não se preocupe em exibir a lista ordenadamente;
print(viagens)

#  Use sorted() para exibir sua lista em ordem alfabética, sem alterar a lista original.
print(sorted_viagens)
# Mostre que sua lista ainda está na ordem original exibindo-a.
print(viagens)

# Use o sorted() para exibir sua lista em ordem alfabética reversa, sem alterar a ordem
sorted_viagens.reverse()
print(sorted_viagens)

# Demonstre que sua lista ainda está na ordem original exibindo-a mais uma vez.
print(viagens)

# Use o reverse() para alterar a ordem de sua lista. Exiba essa lista para mostrar que sua ordem foi alterada.
viagens.reverse()
print(viagens)

# Use o reverse() para alterar a ordem de sua lista novamente. Exiba-a a fim de mostrar que voltou à ordem original.
viagens.reverse()
print(viagens)

# Use o sort() para alterar sua lista para que ela seja armazenada em ordem alfabética. Exiba a lista para mostrar que sua ordem foi alterada.
viagens.sort()
print(viagens)

# Use sort() para alterar sua lista, de modo que ela seja armazenada em ordem alfabética inversa. 
viagens.sort(reverse=True)
print(viagens)

"""
3.9 Convidados para o jantar: Recorra a um dos programas dos exercícios 3.4 a 3.7
(páginas 75-76), e use len() para exibir uma mensagem indicando o número de
pessoas que você está convidando para jantar.
"""
import exercicio8    

exercicio8.convite_convidados(exercicio8.get_convidados())

"""
    3.10 Funções: Pense em coisas que você conseguiria armazenar em uma lista. Por
    exemplo, você pode criar uma lista de montanhas, rios, países, cidades, idiomas, ou
    qualquer outra coisa que quiser. Crie um programa com uma lista contendo esses itens
"""

lista = ["Everest","Aconcágua", "Kilimanjaro", "Amazonas",  "Nilo", "Yangtzé", "Brasil","Japão","Canadá",         
    "Paris", "São Paulo",   "Tóquio","Português", "Inglês","Mandarim"        
]