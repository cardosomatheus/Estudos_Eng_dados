from pathlib import Path
import json

def get_stored_username(path):
    """Obtém o nome de usuário armazenado, se disponível"""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:        
     return None
 
 
def greet_user():
    """Cumprimenta o usuário pelo nome"""
    path = Path('username.json')
    username = get_stored_username(path)
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}!")


def get_new_username(path):
    """Solicita um novo nome de usuário"""
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username
greet_user()