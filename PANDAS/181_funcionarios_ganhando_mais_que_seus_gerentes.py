import pandas as pd

"""
Table: Employee

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| salary      | int     |
| managerId   | int     |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table indicates the ID of an employee, their name, salary, and the ID of their manager.
 

Write a solution to find the employees who earn more than their managers.

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Employee table:
+----+-------+--------+-----------+
| id | name  | salary | managerId |
+----+-------+--------+-----------+
| 1  | Joe   | 70000  | 3         |
| 2  | Henry | 80000  | 4         |
| 3  | Sam   | 60000  | Null      |
| 4  | Max   | 90000  | Null      |
+----+-------+--------+-----------+
Output: 
+----------+
| Employee |
+----------+
| Joe      |
+----------+
Explanation: Joe is the only employee who earns more than his manager.
"""


def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
   # Retorna nome de funcionarios que posssui um salário maio que o salario do seu gerente.
   df_merging = employee.merge(employee, 
                               left_on='managerId',
                               right_on='id',
                               how='inner',
                               suffixes=('_A','_B'))[['name_A','salary_A','salary_B']]
   
   return df_merging[df_merging['salary_A'] > df_merging['salary_B']][['name_A']].rename(columns={'name_A':'Employee'})
   

   


data = [[1, 'Joe', 70000, 3], [2, 'Henry', 80000, 4], [3, 'Sam', 60000, None], [4, 'Max', 90000, None]]
employee = pd.DataFrame(data, columns=['id', 'name', 'salary', 'managerId']).astype({'id':'Int64', 'name':'object', 'salary':'Int64', 'managerId':'Int64'})


pprint.pprint(find_employees(employee=employee))