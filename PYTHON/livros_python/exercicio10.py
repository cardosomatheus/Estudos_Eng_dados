"""
4.1 Pizzas: Pense em, pelo menos, três tipos que você gosta. Armazene esses nomes
de pizza em uma lista e use um loop for para exibir o nome de cada uma.
    • Modifique seu loop for a fim de que exiba uma frase usando o nome da pizza, em
    vez de exibir apenas o nome da pizza. Para cada pizza, você deve gerar uma linha de
    saída com uma simples afirmação como: Gosto de pizza de pepperoni.
    • Adicione uma linha no final do seu programa, fora do loop for, que ressalte o quanto
    você gosta de pizza. A saída deve ter três ou mais linhas sobre os tipos de pizza que
    você gosta e, em seguida, uma frase adicional, como Eu amo pizza!  

"""

pizzas = ['mussarela', 'quatro queijos', 'mussarela']


for pizza in pizzas:
    print(pizza)
    

""" Modifique seu loop for a fim de que exiba uma frase usando o nome da pizza, em
    vez de exibir apenas o nome da pizza. Para cada pizza, você deve gerar uma linha de
    saída com uma simples afirmação como: Gosto de pizza de pepperoni.
"""

for pizza in pizzas: 
    print(f'Gosto da pizza de {pizza} !!!')
print('Como Eu amo pizza!')



""" 
4.2 Animais: Pense em, pelo menos, três animais diferentes que compartilhem uma
    característica comum. Armazene o nome desses animais em uma lista e, em seguida,
    use um loop for para exibir o nome de cada animal.
    • Modifique seu programa a fim de exibir uma afirmação sobre cada animal, como Um
    cachorro seria um ótimo animal de estimação (pet).
    
    • Adicione uma linha no final do seu programa, indicando o que esses animais
    compartilham em comum. Você pode exibir uma frase, como Qualquer um desses
    animais daria um ótimo animal de estimação!
"""

animais = ['jabuti', 'tartaruga', 'Iguana']
for animal in animais:
    print(f'Como seria bom ter um {animal} como animal de estimação (pet).')

print('Todos são répteis')



# 4.3 Contando até vinte: Use um loop for para exibir os números de 1 a 20, todos juntos.
for i in range(1,21):
    print(f'{i}',end='')
    


# 4.4 Um milhão: Crie uma lista com números de um a um milhão e, em seguida, utilize um loop for para exibi-los.
lista_1milhao = list(range(1,1000001))
#for i in lista_1milhao:
#    print(i)


"""
4.5 Somando um milhão: crie uma lista com números de um a um milhão e, em
seguida, use min() e max() a fim de garantir que sua lista realmente comece em um e
termine em um milhão. Além disso, use a função sum() para ver a rapidez com que o
Python pode efetuar a soma de um milhão de números.
"""
print(sum(lista_1milhao))
print(min(lista_1milhao))
print(max(lista_1milhao))


# 4.6 Números ímpares: Use o terceiro argumento da função range() para criar uma lista com números ímpares de 1 a 20. Use o loop for para exibir cada número.

lista_primos = list(range(1,20))



from exercicio6 import factorial
for p in lista_primos:
    if p <= 1:
        continue

    valor_fatorial =  factorial(p-1) +1    
    if valor_fatorial%p == 0:
        print(p)
    

# 4.7 Três: Crie uma lista dos múltiplos de 3, de 3 a 30. Use um loop for para exibir os números em sua lista.

range_30 = list(range(1,30,3))
for value in range_30:
    print(value)




"""
4.8 Cubos: Um número elevado à terceira potência é chamado de cubo. Por exemplo,
no Python, o cubo de 2 é escrito como 2**3. Escreva uma lista dos primeiros 10 cubos
(ou seja, o cubo de cada número inteiro de 1 a 10) e use um loop for para exibir o
valor de cada cubo.


4.9 Cube Comprehension:
"""
value_of_cube = list(range(1,11))
for value in value_of_cube:
    cube = value ** 3
    print(cube)

list_cube_compreenshion = [value**3 for value in value_of_cube]
print(list_cube_compreenshion)