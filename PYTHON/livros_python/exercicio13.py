"""
5.1 Testes condicionais: Escreva uma série de testes condicionais. Exiba uma afirmação
com cada teste descrito e a previsão dos resultados de cada teste. Seu código deve
ficar mais ou menos assim:
    car = 'subaru'
    print("Is car == 'subaru'? I predict True.")
    print(car == 'subaru')
    print("\nIs car == 'audi'? I predict False.")
    print(car == 'audi')
    • Preste bastante atenção aos seus resultados e procure entender por que cada linha
    é avaliada como True ou False.
    • Crie, pelo menos, 10 testes. Execute, pelo menos, 5 testes avaliados como True e
    outros 5 testes avaliados como False.
    • Testes para averiguar se um valor consta em uma lista.
    • Testes para averiguar se um valor não consta em uma lista.    
"""

carros = ['subaru','toyota','honda','ford','chevrolet','bmw','audi','mercedes','volkswagen','nissan']
for carro in carros:
    chute_carro = str(input('informe seu chute do carro: '))

    if carro == chute_carro:
        print(f"Is car == {chute_carro}? I predict True.")
        print(carro == 'subaru')
    else:
        print(f"\nIs car == {chute_carro}? I predict False.")
        print(carro == 'audi')

print()

chute_carro = str(input('informe seu chute do carro: '))
if chute_carro in carros:
    print('existe')
else:
    print('Não existe')