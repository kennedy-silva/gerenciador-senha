import sqlite3

MASTER_PASSWORD = '123456'

senha = input('Insira sua senha master: ')
if senha != MASTER_PASSWORD:
    print('Senha inválida.Encerrando...')
    exit()

connection = sqlite3.connect('passwords.db')

cursor = connection.cursor()

cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    service  TEXT NOT NULL,
                    username TEXT NOT NULL,
                    password TEXT NOT NULL);''')


def menu():
    print('*****************************')
    print('* i: inserir nova senha     *')
    print('* l: listar serviços salvos *')
    print('* r: recuperar uma senha    *')
    print('* s: sair                   *')
    print('*****************************')


def get_password(service):
    cursor.execute(f'''
                    SELECT username, password FROM users
                    WHERE service = '{service}'
                    ''')

    if cursor.rowcount == 0:
        print("Serviço não cadastrado (use '1' para verificar os serviços).")
    else:
        for user in cursor.fetchall():
            print(user)

def insert_passwords(service, username, password):
    cursor.execute(f'''
                    INSERT INTO users (service, username, password)
                    VALUES ('{service}', '{username}', '{password}')''')
    connection.commit()

def show_services():
    cursor.execute('''
                    SELECT  service FROM users;''')
    for service in cursor.fetchall():
        print(service)

while True:
    menu()
    opcao = input('O que deseja fazer? ')
    if opcao not in ['i', 'l', 'r', 's']:
        print('Opção inválida!')
        continue

    if opcao == 's':
        break

    if opcao == 'i':
        service = input('Qual o seu serviço? ')
        username = input('Qual o seu usuário? ')
        password = input('Qual a sua senha? ')
        insert_passwords(service, username, password)

    if opcao == 'l':
        show_services()

    if opcao == 'r':
        service = input('Qual o serviço para o qual quer a senha? ')
        get_password(service)

connection.close()
