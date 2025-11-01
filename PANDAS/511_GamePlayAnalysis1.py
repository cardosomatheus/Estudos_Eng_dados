"""
+--------------+---------+ 
| Nome da Coluna | Tipo | 
+--------------+---------+ 
| player_id | int | 
| device_id | int | 
| event_date | date | 
| games_played | int | 
+--------------+---------+ 
(player_id, event_date) é a chave primária (combinação de colunas com valores únicos) desta tabela. 
Esta tabela mostra a atividade de jogadores em alguns jogos. 
Cada linha é um registro de um jogador que fez login e jogou um número de partidas (possivelmente 0) antes de fazer logout em algum dia, usando algum dispositivo.
 

Escreva uma solução para encontrar a data do primeiro login de cada jogador.

Retorne a tabela de resultados em qualquer ordem .

O formato do resultado está no exemplo a seguir.

 

Exemplo 1:

Entrada:  
Tabela de atividades: 
+-----------+-----------+------------+--------------+ 
| player_id | device_id | event_date | games_played | 
+-----------+-----------+------------+--------------+ 
| 1 | 2 | 2016-03-01 | 5 | 
| 1 | 2 | 2016-05-02 | 6 | 
| 2 | 3 | 2017-06-25 | 1 | 
| 3 | 1 | 2016-03-02 | 0 | 
| 3 | 4 | 2018-07-03 | 5 | 
+-----------+-----------+------------+--------------+ Saída: 
+-----------+-------------+ 
| player_id | first_login | 
+-----------+-------------+ 
| 1 | 01/03/2016 | 
| 2 | 25/06/2017 | 
| 3 | 02/03/2016 | 
+-----------+-------------+
"""

import pandas as pd

data = [[1, 2, '2016-03-01', 5], [1, 2, '2016-05-02', 6], [2, 3, '2017-06-25', 1], [3, 1, '2016-03-02', 0], [3, 4, '2018-07-03', 5]]
activity = pd.DataFrame(data, columns=['player_id', 'device_id', 'event_date', 'games_played']).astype({'player_id':'Int64', 'device_id':'Int64', 'event_date':'datetime64[ns]', 'games_played':'Int64'})


def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    # retorna o primeiro login de cada player.
    return activity.groupby(by=['player_id'], as_index=False)['event_date'].min()\
           .rename(columns={'event_date':'first_login'})

