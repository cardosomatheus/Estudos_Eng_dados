"""
+---------------+---------+
| Nome da coluna | Tipo |
+---------------+---------+
| id | int |
| dataDeRegistro | data |
| temperatura | int |
+---------------+---------+
"id" é a coluna com valores únicos para esta tabela.
Não existem linhas diferentes com a mesma data de registro.
Esta tabela contém informações sobre a temperatura em um determinado dia.
 

Escreva uma solução para encontrar todas as datas idcom temperaturas mais altas em comparação com as datas anteriores (ontem).

Retorne a tabela de resultados em qualquer ordem .

O formato do resultado está no exemplo a seguir.

 

Exemplo 1:

Entrada: 
Tabela meteorológica:
+----+------------+-------------+
| id | data do registro | temperatura |
+----+------------+-------------+
| 1 | 01/01/2015 | 10 |
| 2 | 02/01/2015 | 25 |
| 3 | 03/01/2015 | 20 |
| 4 | 04/01/2015 | 30 |
+----+------------+-------------+
Saída: 
+----+
| id |
+----+
| 2 |
| 4 |
+----+
Explicação: 
Em 02/01/2015, a temperatura foi mais alta do que no dia anterior (10 -> 25).
Em 04/01/2015, a temperatura foi mais alta do que no dia anterior (20 -> 30).
"""
import pandas as pd


data = [[1, '2015-01-01', 10], [2, '2015-01-02', 25], [3, '2015-01-03', 20], [4, '2015-01-04', 30]]
weather = pd.DataFrame(data, columns=['id', 'recordDate', 'temperature']).astype({'id':'Int64', 'recordDate':'datetime64[ns]', 'temperature':'Int64'})

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    # Cria um campo com data -1
    weather['recordDatePrev'] = weather['recordDate'] - pd.Timedelta(days=1)
    # Merge baseado na data x data_anterior
    weather = weather.merge(weather, how='left', left_on='recordDate', right_on= 'recordDatePrev')

    #Filtra apenas temperatura cuja a temperatura do dia posterior foi maior
    weather = weather[weather['temperature_y'] > weather['temperature_x']].rename(columns={'id_y':'id'})

    return weather[['id']]

    
print(rising_temperature(weather=weather))