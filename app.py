import sqlite3

def conexao_banco():
    conexao =  sqlite3.connect('contatos.db')
    cursor = conexao.cursor()

    sql = '''CREATE TABLE IF NOT EXISTS contatos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        telefone TEXT NOT NULL,
        email TEXT NOT NULL
    )'''

    cursor.execute(sql)
    conexao.commit()
    return conexao

def adicionar_contato(nome, telefone, email):
    conexao = conexao_banco()
    cursor = conexao.cursor()

    sql = '''
        INSERT INTO contatos (nome, telefone, email) VALUES (?, ?, ?)'''
    cursor.execute(sql, (nome, telefone, email))
    conexao.commit()
    conexao.close()

def listar_contatos():
    conexao = conexao_banco()
    cursor = conexao.cursor()
    sql = '''
        SELECT * FROM contatos'''

    cursor.execute(sql)
    contatos = cursor.fetchall()

    if len(contatos) == 0:
        print('Nenhum contato encontrado.')
    else:
        print('### Lista de Contatos ###')
        print (f'{'ID':<5} {'Nome':<20} {'Telefone':<15} {'Email':<30}')
        print('-' * 60)
        for contato in contatos:
            print(f'ID: {contato[0]}, Nome: {contato[1]}, Telefone: {contato[2]}, Email: {contato[3]}')
    
    conexao.close()

def buscar_contato():
    conexao = conexao_banco()
    cursor = conexao.cursor()

    nome = input('Digite o nome do contato que deseja buscar: ')
    sql = '''
        SELECT * FROM contatos WHERE nome LIKE ?'''
    cursor.execute(sql, ('%' + nome + '%',))
    print('### Contatos encontrados ###')
    print (f'{'ID':<5} {'Nome':<20} {'Telefone':<15} {'Email':<30}')
    print('-' * 60)

    contatos = cursor.fetchall()

    for contato in contatos:
        print(f'ID: {contato[0]}, Nome: {contato[1]}, Telefone: {contato[2]}, Email: {contato[3]}')

    conexao.close()

def atualizar_contato():
    conexao = conexao_banco()
    cursor = conexao.cursor()
    id_contato = input('Digite o ID do contato que deseja atualizar: ')
    nome = input('Digite o novo nome do contato: ')
    telefone = input('Digite o novo telefone do contato: ')
    email = input('Digite o novo email do contato: ')

    sql = '''
        UPDATE contatos SET nome = ?, telefone = ?, email = ? WHERE id = ?'''
    cursor.execute(sql, (nome, telefone, email, id_contato))
    conexao.commit()
    conexao.close()

def excluir_contato():
    conexao = conexao_banco()
    cursor = conexao.cursor()
    id_contato = input('Digite o ID do contato que deseja excluir: ')

    sql = '''
        DELETE FROM contatos WHERE id = ?'''
    cursor.execute(sql, (id_contato,))

    if cursor.rowcount == 0: #rowcount retorna o numero de linhas alteradas ou excluidas na ultima execução do comando
        print('Contato não encontrado.')
    else:
        print('Contato excluído com sucesso.')

    conexao.commit()
    conexao.close()

def menu():
    while True:
        print('### Contatos ###')
        print('1 - Adicionar contato')
        print('2 - Listar contatos')
        print('3 - Buscar contato pelo nome')
        print('4 - Atualizar contato')
        print('5 - Excluir contato')
        print('0 - Sair')

        opcao = input('Escolha uma opção: ')
        if opcao == '1':
            nome = input('Digite o nome do contato: ')
            telefone = input('Digite o telefone do contato: ')
            email = input('Digite o email do contato: ')
            
            adicionar_contato(nome, telefone, email)
            print('Contato adicionado com sucesso!')
        elif opcao == '2': 
            listar_contatos()
        elif opcao == '3':
            buscar_contato()
        elif opcao == '4':
            atualizar_contato()
        elif opcao == '5':
            excluir_contato()
        elif opcao == '0':
            print('Saindo do sistema...')
            break

menu()