#1. O volume de uma esfera com raio r é . Qual é o volume de uma esfera com raio 5?
#Fórmula do volume da esfera:
# V = (4/3) * π * r³

raio = (4/3) * 5**3
valor_pi = 3.14159

print(f'{raio * valor_pi:.2f} unidade cubicas.')


"""2. Suponha que o preço de capa de um livro seja R$ 24,95, mas as livrarias recebem um desconto de 40%. O transporte custa R$ 3,00
para o primeiro exemplar e 75 centavos para cada exemplar adicional. Qual é o custo totalde atacado para 60 cópias?
"""
def calcular_valor_total_capas(valor_por_capa: float, qtd_unidades: int, valor_do_desconto: float):

    valor_total_para_compra_das_capas = valor_por_capa * qtd_unidades 
    valor_total_das_capas_apos_desconto =  valor_total_para_compra_das_capas - (valor_total_para_compra_das_capas*valor_do_desconto/100)

    valor_total_para_transporte_das_capas = 3 + ((qtd_unidades-1) * 0.75) # (59 capas * 75 centavos) + 1 capa de 3 reais
    valor_total_da_compra = valor_total_das_capas_apos_desconto+valor_total_para_transporte_das_capas    
    

    print()
    print(f'O custo total para transporte de capas é {valor_total_para_transporte_das_capas}') 
    print(f'Valor após o desconto de 40% {valor_total_da_compra}')


calcular_valor_total_capas(valor_por_capa=24.95, qtd_unidades=60, valor_do_desconto=40)

"""3. Se eu sair da minha casa às 6:52 e correr 1 quilômetro a um certo passo (8min15s por quilômetro), então 3 quilômetros 
a um passo mais rápido (7min12s por quilômetro) e 1 quilômetro no mesmo passo usado em primeiro lugar, que horas chego em casa para o café da manhã
"""
from datetime import timedelta, datetime

hora_saida = datetime.strptime('06:52','%H:%M')
print(hora_saida)

# Ritmos (minutos e segundos separados)
ritmo1 = timedelta(minutes=8, seconds=15)
ritmo2 = timedelta(minutes=7, seconds=12)
ritmo3 = timedelta(minutes=8, seconds=15)

# Distâncias
tempo_total = ritmo1 + (3 * ritmo2) + ritmo3

# Hora de chegada
hora_chegada = hora_saida + tempo_total

print(hora_chegada)
