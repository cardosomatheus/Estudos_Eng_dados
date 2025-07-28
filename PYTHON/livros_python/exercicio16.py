users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")


responses = {}
# Define uma flag para sinalizar que a pesquisa está ativa
polling_active = True
while polling_active:
# Solicita o nome e a resposta do participante
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    # Armazena a resposta no dicionário
    responses[name] = response
    # Detecta se mais alguém participará da pesquisa
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False
        # A pesquisa está completa. Mostra os resultados.
        print("\n--- Poll Results ---")
    for name, response in responses.items():
        print(f"{name} would like to climb {response}.")    