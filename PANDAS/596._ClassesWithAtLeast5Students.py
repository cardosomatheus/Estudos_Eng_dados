"""
Mesa:Courses

+-------------+---------+
| Nome da coluna | Tipo |
+-------------+---------+
| aluno | varchar |
| classe | varchar |
+-------------+---------+
(aluno, turma) é a chave primária (combinação de colunas com valores únicos) para esta tabela.
Cada linha desta tabela indica o nome de um aluno e a turma em que ele está matriculado.
 

Escreva uma solução para encontrar todas as turmas que têm pelo menos cinco alunos .

Retorne a tabela de resultados em qualquer ordem .

O formato do resultado está no exemplo a seguir.

 

Exemplo 1:

Entrada: 
Tabela de cursos:
+---------+----------+
| aluno | turma |
+---------+----------+
| A | Matemática |
| B | Inglês |
| C | Matemática |
| D | Biologia |
| E | Matemática |
| F | Computador |
| G | Matemática |
| H | Matemática |
| Eu | Matemática |
+---------+----------+
Saída: 
+---------+
| aula |
+---------+
| Matemática |
+---------+
Explicação: 
- A turma de matemática tem 6 alunos, então a incluímos.
- A aula de inglês tem 1 aluno, então não a incluímos.
- A disciplina de Biologia tem 1 aluno, então não a incluímos.
- O computador tem 1 aluno, então não o incluímos.
"""
import pandas as pd

data = [['A', 'Math'], ['B', 'English'], ['C', 'Math'], ['D', 'Biology'], ['E', 'Math'], ['F', 'Computer'], ['G', 'Math'], ['H', 'Math'], ['I', 'Math']]
courses = pd.DataFrame(data, columns=['student', 'class']).astype({'student':'object', 'class':'object'})


def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    quantity_students =  courses['class'].value_counts().reset_index(name='qtd_student')
    filter_5_students = quantity_students[quantity_students['qtd_student'] >= 5]['class']
    return pd.DataFrame(filter_5_students)

