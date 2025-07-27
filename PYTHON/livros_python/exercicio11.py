

"""
4.10 Fatias: Use um dos programas que escreveu neste capítulo, adicione diversas
linhas ao final do programa para executarem o seguinte:
    • Exiba a mensagem: Os três primeiros elementos da lista são:. Em seguida, use uma
    fatia para exibir os três primeiros elementos da lista desse programa.
    • Exiba a mensagem: O três elementos que ficam no meio da lista são:. Depois, use
    uma fatia para exibir os três elementos do meio da lista.
    • Exiba a mensagem: Os três últimos elementos da lista são: Em seguida, utilize uma
    fatia para exibir os três últimos elementos da lista.

"""

lista = ["Everest","Aconcágua", "Kilimanjaro", "Amazonas",  "Nilo", "Yangtzé", "Brasil","Japão","Canadá",         
    "Paris", "São Paulo",   "Tóquio","Português", "Inglês","Mandarim"        
]
print('Os três primeiros elementos da lista são: \n')
for value in lista[:3]:
    print(value)

meio_da_lista = int(len(lista)/2)
print('O três elementos que ficam no meio da lista são: \n')
for value in lista[meio_da_lista:meio_da_lista+3]:
    print(value)

print('Os três últimos elementos da lista são: \n')
for value in lista[-3:]:
    print(value)

"""
4.11 Minhas pizzas, suas pizzas: Comece com o programa do Exercício 4.1 (página 90).
Faça uma cópia da lista de pizzas e a nomeie como friend_pizzas. Em seguida, siga as
etapas:
• Adicione uma pizza nova à lista original.
• Adicione uma pizza diferente à lista friend_pizzas.
• Prove que tem duas listas separadas. Exiba a mensagem: Minhas pizzas favoritas
são:. E, em seguida, use um loop for para exibir a primeira lista. Exiba a mensagem:
Minhas pizzas favoritas são:. E, em seguida, use um loop for para exibir a segunda
lista. 
"""
pizzas = ['mussarela', 'quatro queijos', 'mussarela']
pizzas_friends = pizzas.copy()

pizzas.append('calabresa')
pizzas_friends.append('catupiri')

print('Minhas pizzas favoritas são: \n')
for pizza in pizzas_friends:
    print(pizzas)
    
print('Minhas pizzas favoritas são: \n')
for pizza in pizzas_friends:
    print(pizzas)

