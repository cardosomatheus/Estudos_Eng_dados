"""+-------------+---------+
| Nome da coluna | Tipo |
+-------------+---------+
| idEmp | inteiro |
| nome | varchar |
| supervisor | int |
| salário | int |
+-------------+---------+
empId é a coluna com valores únicos para esta tabela.
Cada linha desta tabela indica o nome e o ID de um funcionário, além de seu salário e o ID de seu gerente.
 

Mesa:Bonus

+-------------+------+
| Nome da coluna | Tipo |
+-------------+------+
| idEmp | inteiro |
| bônus | int |
+-------------+------+
empId é a coluna de valores únicos desta tabela.
empId é uma chave estrangeira (coluna de referência) para empId da tabela Employee.
Cada linha desta tabela contém o ID de um funcionário e seu respectivo bônus.
 

Elabore uma solução para apresentar o nome e o valor do bônus de cada funcionário cujo bônus seja inferior a 1000 .

Retorne a tabela de resultados em qualquer ordem .

O formato do resultado está no exemplo a seguir.

 

Exemplo 1:

Entrada: 
Tabela de funcionários:
+-------+--------+------------+--------+
| ID do funcionário | nome | supervisor | salário |
+-------+--------+------------+--------+
| 3 | Brad | nulo | 4000 |
| 1 | João | 3 | 1000 |
| 2 | Dan | 3 | 2000 |
| 4 | Thomas | 3 | 4000 |
+-------+--------+------------+--------+
Tabela de bônus:
+-------+-------+
| ID do funcionário | bônus |
+-------+-------+
| 2 | 500 |
| 4 | 2000 |
+-------+-------+
Saída: 
+------+-------+
| nome | bônus |
+------+-------+
| Brad | nulo |
| João | nulo |
| Dan | 500 |
+------+-------+
"""


import pandas as pd

data = [[3, 'Brad', None, 4000], [1, 'John', 3, 1000], [2, 'Dan', 3, 2000], [4, 'Thomas', 3, 4000]]
employee = pd.DataFrame(data, columns=['empId', 'name', 'supervisor', 'salary']).astype({'empId':'Int64', 'name':'object', 'supervisor':'Int64', 'salary':'Int64'})
data = [[2, 500], [4, 2000]]
bonus = pd.DataFrame(data, columns=['empId', 'bonus']).astype({'empId':'Int64', 'bonus':'Int64'})


def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    # Retorna funcinarios sem bonus ou menor que mill
    employee_and_bonus = employee.merge(bonus, how='left', left_on='empId', right_on='empId')[['empId','name', 'bonus']]
    return employee_and_bonus[(employee_and_bonus['bonus'] < 1000) | (employee_and_bonus['bonus'].isnull())]


print(employee_bonus(employee=employee, bonus=bonus))