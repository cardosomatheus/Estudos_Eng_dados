## Exercício 1

#1. Quantos segundos há em 42 minutos e 42 segundos?
print(f'{(42 + (42/60)) * 60} segundos.')

#2. Quantas milhas há em 10 quilômetros? Dica: uma milha equivale a 1,61 quilômetro.
print(f'{10/1.61:.2f} milhas')

#3. Se você correr 10 quilômetros em 42 minutos e 42 segundos, qual é o seu passo médio (tempo por milha em minutos e segundos)? Qual é a sua
#velocidade média em milhas por hora?
milhas = 10/1.61 # km para milha
total_minutos = 42 + (42/60)

velocidade_media_por_minutos = total_minutos/milhas
minutos  =  int(velocidade_media_por_minutos)
segundos = int((velocidade_media_por_minutos - minutos) *60)

total_horas = total_minutos/60
velocidade_media_por_hora = milhas/total_horas

print(f'passo medio de {minutos} minutos e {segundos} segundos.')
print(f'velocidade média em milhas por hora: {velocidade_media_por_hora:.2f}')
