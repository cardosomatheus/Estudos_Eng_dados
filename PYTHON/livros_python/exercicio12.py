""" 
4.13 Buffet: Um restaurante com serviço de buffet oferece somente cinco refeições
básicas. Pense em cinco refeições simples e armazene-as em uma tupla.
    • Use um loop for para exibir cada refeição que o restaurante oferece.
    • Tente modificar um dos elementos e verifique se o Python rejeita a mudança. (tuplas são imutaveis, a unica forma é sobreescreve-la)
    • O restaurante muda seu cardápio, substituindo dois dos elementos por refeições
    diferentes. Adicione uma linha que reescreva a tupla e, depois, use um loop for para
    exibir cada um dos elementos no menu reformulado.
"""

alimentos = ('arroz', 'feijao','carne','salada','laranja')
for alimento in alimentos:
    print(alimento)

print()

alimentos = alimentos = ('arroz', 'feijao','carne','salada','limão')
for alimento in alimentos:
    print(alimento)



