"""
Mesa:World

+-------------+---------+ 
| Nome da Coluna | Tipo | 
+-------------+---------+ 
| nome | varchar | 
| continente | varchar | 
| área | int | 
| população | int | 
| PIB | bigint | 
+-------------+---------+ 
O nome é a chave primária (coluna com valores únicos) desta tabela. 
Cada linha desta tabela fornece informações sobre o nome de um país, o continente ao qual pertence, sua área, a população e o valor do seu PIB.
 

Um país é grande se:

tem uma área de pelo menos três milhões (ou seja, ), ou3000000 km2
tem uma população de pelo menos vinte e cinco milhões (ou seja, 25000000).
Escreva uma solução para encontrar o nome, a população e a área dos maiores países .

Retorne a tabela de resultados em qualquer ordem .

O formato do resultado está no exemplo a seguir.

 

Exemplo 1:

Entrada:  
Tabela mundial: 
+-------------+-----------+---------+------------+--------------+ 
| nome | continente | área | população | PIB | 
+-------------+-----------+---------+------------+--------------+ 
| Afeganistão | Ásia | 652230 | 25500100 | 20343000000 | 
| Albânia | Europa | 28748 | 2831741 | 12960000000 | 
| Argélia | África | 2381741 | 37100000 | 188681000000 | 
| Andorra | Europa | 468 | 78115 | 3712000000 | 
| Angola | África | 1246700 | 20609294 | 100990000000 | 
+-------------+-----------+---------+------------+--------------+ Saída: 
+-------------+------------+---------+ 
| nome | população | área | 
+-------------+------------+---------+ 
| Afeganistão | 25500100 | 652230 | 
| Argélia | 37100000 | 2381741 | 
+-------------+------------+---------+
"""

import pandas as pd
    
data = [['Afghanistan', 'Asia', 652230, 25500100, 20343000000], ['Albania', 'Europe', 28748, 25000000, 12960000000], ['Algeria', 'Africa', 2381741, 37100000, 188681000000], ['Andorra', 'Europe', 468, 78115, 3712000000], ['Angola', 'Africa', 1246700, 20609294, 100990000000]]
world = pd.DataFrame(data, columns=['name', 'continent', 'area', 'population', 'gdp']).astype({'name':'object', 'continent':'object', 'area':'Int64', 'population':'Int64', 'gdp':'Int64'})

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    # Paises com população maior/igual que 25000000 ou area maior/igual que 3000000
    return world[(world['area'] >= 3000000) | ((world['population'] >= 25000000))][['name', 'population','area']]

print(big_countries(world=world))