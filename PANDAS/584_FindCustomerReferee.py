"""
Mesa:Customer

+-------------+---------+
| Nome da coluna | Tipo |
+-------------+---------+
| id | int |
| nome | varchar |
| id_do_árbitro | inteiro |
+-------------+---------+
Em SQL, o campo "id" é a coluna de chave primária desta tabela.
Cada linha desta tabela indica o ID de um cliente, seu nome e o ID do cliente que o indicou.
 

Encontre os nomes dos clientes que são:

indicado por  qualquer cliente com  id != 2.
Não foi indicado por nenhum cliente.
Retorne a tabela de resultados em qualquer ordem .

O formato do resultado está no exemplo a seguir.

 

Exemplo 1:

Entrada: 
Tabela de clientes:
+----+------+------------+
| id | nome | id_do_referente |
+----+------+------------+
| 1 | Vontade | nulo |
| 2 | Jane | nulo |
| 3 | Alex | 2 |
| 4 | Projeto de Lei | nulo |
| 5 | Zack | 1 |
| 6 | Marca | 2 |
+----+------+------------+
Saída: 
+------+
| nome |
+------+
| Vontade |
| Jane |
| Conta |
| Zack |
"""

import pandas as pd
    

data = [[1, 'Will', None], [2, 'Jane', None], [3, 'Alex', 2], [4, 'Bill', None], [5, 'Zack', 1], [6, 'Mark', 2]]
customer = pd.DataFrame(data, columns=['id', 'name', 'referee_id']).astype({'id':'Int64', 'name':'object', 'referee_id':'Int64'})


def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    # Retorna todos customer exceto aqueles com referee_id = 2
    return customer[(customer['referee_id'] != 2 ) | (customer['referee_id'].isna())]
    


print(find_customer_referee(customer=customer))


