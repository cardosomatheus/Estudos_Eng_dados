"""
Table: Person

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| email       | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table contains an email. The emails will not contain uppercase letters.
 

Write a solution to delete all duplicate emails, keeping only one unique email with the smallest id.

For SQL users, please note that you are supposed to write a DELETE statement and not a SELECT one.

For Pandas users, please note that you are supposed to modify Person in place.

After running your script, the answer shown is the Person table. The driver will first compile and run your piece of code and then show the Person table. The final order of the Person table does not matter.
"""

import pandas as pd

data = [[1, 'john@example.com'], [3, 'john@example.com'], [2, 'bob@example.com']]
person = pd.DataFrame(data, columns=['id', 'email']).astype({'id':'int64', 'email':'object'})


def delete_duplicate_emails(person: pd.DataFrame) -> None:
    # 1: Ordenamos o Dataframe pela coluna ID
    person.sort_values(by=["id"],ascending=True, inplace=True)
    
    # 2: Deletamos emails duplicados mantendo sempre o ID menor
    person.drop_duplicates(subset=["email"],keep='first',inplace=True)


delete_duplicate_emails(person=person)
print(person)