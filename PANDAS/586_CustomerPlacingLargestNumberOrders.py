"""Mesa:Orders

+-----------------+----------+
| Nome da coluna | Tipo |
+-----------------+----------+
| número_do_pedido | inteiro |
| número_do_cliente | inteiro |
+-----------------+----------+
order_number é a chave primária (coluna com valores únicos) desta tabela.
Esta tabela contém informações sobre o ID do pedido e o ID do cliente.
 

Escreva uma solução para encontrar customer_numbero cliente que fez o maior número de pedidos .

Os casos de teste são gerados de forma que exatamente um cliente tenha feito mais pedidos do que qualquer outro cliente.

O formato do resultado está no exemplo a seguir.

 

Exemplo 1:

Entrada: 
Tabela de pedidos:
+--------------+-----------------+
| número_do_pedido | número_do_cliente |
+--------------+-----------------+
| 1 | 1 |
| 2 | 2 |
| 3 | 3 |
| 4 | 3 |
+--------------+-----------------+
Saída: 
+-----------------+
| número_do_cliente |
+-----------------+
| 3 |
+-----------------+
Explicação: 
O cliente número 3 tem dois pedidos, o que é maior do que os clientes 1 e 2, pois cada um deles tem apenas um pedido.
Portanto, o resultado é o cliente número 3.
"""

import pandas as pd

    
data = [[1, 1], [2, 2], [3, 5], [4, 5]]
orders = pd.DataFrame(data, columns=['order_number', 'customer_number']).astype({'order_number':'Int64', 'customer_number':'Int64'})

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    # Agrupa por customer_number e dar um alias ao count() de countvalues
    # Ordena pelo maior valor de countvalues desc
    # Retorna o primeiro
    return orders.groupby('customer_number')['order_number'].count().reset_index(name='countvalues')\
                 .sort_values(by='countvalues', ascending=False)\
                 .head(1)[['customer_number']]
