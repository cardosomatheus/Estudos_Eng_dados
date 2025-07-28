"""
5.3 Cores de alienígenas #1: Imagine que um alienígena acabou de ser abatido em um
jogo. Crie uma variável chamada alien_color e lhe atribua um valor 'green', 'yellow' ou
'red'.
    • Escreva uma instrução if para testar se a cor do alienígena é verde. Se for, exiba
    uma mensagem informando que o jogador acabou de ganhar 5 pontos.

5.4 Cores de alienígenas #2: Escolha uma cor para um alienígena, como no
Exercício 5.3, e escreva uma sequência if-else.
    • Se a cor do alienígena for verde, exiba uma afirmação de que o jogador acabou de
    ganhar 5 pontos por abrir fogo contra um alienígena.
    • Se a cor do alienígena não for verde, exiba uma afirmação de que o jogador acabou
    de ganhar 10 pontos.
    • Escreva uma versão desse programa que execute o bloco if e outra que execute o
    bloco else.
5.5 Cores alienígenas #3: Converta sua sequência if-else do Exercício 5.4 em uma
sequência if-elif-else.
    • Se o alienígena for verde, exiba uma afirmação de que o jogador ganhou 5 pontos.
    • Se o alienígena for amarelo, exiba uma afirmação de que o jogador ganhou
    10 pontos.
    • Se o alienígena for vermelho, exiba uma afirmação de que o jogador ganhou
    15 pontos.
    • Escreva três versões desse programa, assegurando que cada afirmação exibida seja
    correspondente à cor adequada do alienígena
5.6 Fases da vida: Escreva uma sequência if-elif-else que determine a fase da vida de
    uma pessoa. Defina um valor para a variável age, e depois:
    • Se a pessoa tiver menos de 2 anos, exiba uma mensagem informando que a pessoa
    é um neném.
    Se a pessoa tiver pelo menos 2 anos, e menos de 4, exiba uma mensagem
    informando que é uma criança.
    • Se a pessoa tiver pelo menos 4 anos, e menos de 13, exiba uma mensagem
    informando que é um(a) garoto(a).
    • Se a pessoa tiver pelo menos 13 anos, e menos de 20, exiba uma mensagem
    informando que é adolescente.
    • Se a pessoa tiver pelo menos 20 anos, e menos de 65, exiba uma mensagem
    informando que é um adulto.
    • Se a pessoa tiver 65 anos ou mais, imprima uma mensagem informando que a
    pessoa é um(a) idoso(a).
5.7 Fruta favorita: Crie uma lista de suas frutas favoritas e, em seguida, escreva uma
    série de declarações if independentes que verificam determinadas frutas em sua lista.
    • Crie uma lista com suas três frutas favoritas e a nomeie como favorite_fruits.
    • Escreva cinco instruções if. Cada uma deve verificar se um determinado tipo de fruta
    consta em sua lista. Se sim, o bloco if deve exibir uma afirmação do tipo: Você
    realmente gosta de bananas!
"""

alien_color = str(input('Escolha uma cor: (green, yellow,red) '))

if alien_color.lower() == 'green':
    print('+5 pontos')
elif alien_color.lower() == 'yellow':
    print('+10 pontos')

elif alien_color.lower() == 'red':
    print('+15 pontos')

else:
    print('+10 pontos')


age = 2

if age < 2 :
    print('neném')    
elif age < 4 :
    print('crianca')    

elif age < 13 :
    print('garoto(a)')   

elif age < 20 :
    print('adolescente')

elif age < 65 :
    print('adulto')

elif age >= 65 :
    print('idoso')
    


favorite_fruits = ['banana','limao','laranja','maça','abacaxi']

for fruta in favorite_fruits:
    if fruta in favorite_fruits:
        print(f'Você realmente gosta de {fruta} !!')
        