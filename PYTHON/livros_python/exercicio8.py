"""
Os exercícios seguintes são um pouco mais complexos do que os do Capítulo 2, mas
lhe possibilitam usar as listas de todas as formas descritas.

3.4 Lista de convidados: Se pudesse convidar qualquer pessoa, viva ou falecida, para
um jantar, quem você convidaria? Crie uma lista que tenha pelo menos três pessoas
que gostaria de convidar para um jantar. Em seguida, use sua lista a fim de exibir uma
mensagem para cada pessoa, convidando-a para o jantar
"""

convidados = ['Jackie chan', 'Michael Jackson', 'Soluço']
ja_convidados = []

def get_convidados():
    return convidados

def convite_convidados (lista_convidados, ind_confirma_convites = 0):

    if not isinstance(lista_convidados, list):
        print('o parametro de lista_convidados é um List, informe corretamente.')
        return
    
    if len(lista_convidados) == 0:
        print('A lista de convidados está vazia')
        return
    
    print()

        
    contador = 0
    while contador < len(lista_convidados):
        if convidados[contador] not in ja_convidados:
            print(f'{lista_convidados[contador].title()}, Gostaria de convidar para um jantar da comunidade?') 
            ja_convidados.append(convidados[contador])
        
        elif convidados[contador] in ja_convidados and ind_confirma_convites == 1:
            print(f'{lista_convidados[contador].title()}, Confirmo o convie para o jantar.') 


        contador +=1        
    print(f'{len(lista_convidados)} foram convidadas no total')
    print()

"""
3.5 Mudando a lista de lista_convidados: Você acabou de ficar sabendo que um dos
convidados não conseguirá ir ao jantar, assim precisa enviar um conjunto novo de
convites. É necessário convidar outra pes
    • Comece com o programa do Exercício 3.4. No final do programa, adicione um print(),
    informando o nome do convidado que não irá ao jantar.
    • Modifique sua lista substituindo o nome do convidado que não pode comparecer pelo
    nome da pessoa nova que você está convidando.
    • Exiba um segundo conjunto de mensagens de convite, uma para cada pessoa que
    ainda não consta em sua lista.
"""

convite_convidados(convidados)

print(f'O {convidados[0]} teve que sair as pressas,mas ele convidou um representante de alto valor em seu lugar. \n')

del convidados[0]
convidados.insert(0,'Bruce Lee')
convite_convidados(convidados)


"""
3.6 Mais convidados: Você acabou de encontrar uma mesa maior de jantar, agora há
mais espaço disponível. Convide mais três pessoas para o jantar.
• Comece com o programa do Exercício 3.4 ou 3.5. No final do programa, adicione um
print(), informando às pessoas que encontrou uma mesa maior.
• Use um insert() para adicionar um convidado novo ao início de sua lista.
• Use um insert() para adicionar um convidado novo no meio de sua lista.
• Use um append() para adicionar um convidado novo no final de sua lista.
• Exiba um

"""


print('encontrei uma mesa maior.\n')
convidados.insert(0,'Kaneki')
convidados.insert(int(len(convidados)/2)+1,'Flash')
convidados.insert(len(convidados),'Ragnar')

convite_convidados(convidados)

"""
3.7 Reduzindo a lista de convidados: Você acabou de descobrir que sua mesa nova de
jantar não chegará a tempo e agora tem espaço somente para dois convidados.
    • Comece com o programa do Exercício 3.6. Adicione uma linha nova que exiba uma
    mensagem que você pode convidar apenas duas pessoas para o jantar.
    • Use o pop() para remover convidados de sua lista, um de cada vez, até que restem
    somente dois nomes nela. Sempre que remover um nome de sua lista, exiba uma
    mensagem para essa pessoa informando que lamenta por não poder convidá-la para
    o jantar.
    • Exiba uma mensagem para cada uma das duas pessoas que ainda estão na sua lista,
    informando que ainda estão convidadas.
    • Use o del para remover os dois últimos nomes de sua lista, para que ela fique vazia.
    Exiba sua lista para ter certeza de que você realmente tem uma lista vazia no final do
    seu programa.
"""

def desconvida_convidados(lista_convidados):
    if not isinstance(lista_convidados, list):
        print('o parametro de lista_convidados é um List, informe corretamente.')
        return
    
    if len(lista_convidados) == 0:
        print('A lista de convidados está vazia')
        return
        
    contador = 0
    lista_com_2_registros = len(lista_convidados) -2 
    while contador < lista_com_2_registros:

        print(f'lamento por não poder convidá-la para o jantar {convidados[-1]}.')
        convidados.pop()
        contador +=1

    print()

desconvida_convidados(convidados)
convite_convidados(convidados,1)

del convidados[0]
del convidados[0]
ja_convidados = convidados
print(ja_convidados)
print(convidados)