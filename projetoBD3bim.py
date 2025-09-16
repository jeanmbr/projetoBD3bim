from prettytable import PrettyTable
import mysql.connector

def ativabanco():
    try:
        global conexao
        conexao = mysql.connector.connect(
            host='localhost',
            database='projeto3bim',
            user='root',
            password=''
        )
        if conexao.is_connected():
            print('-='*62)
            print('{:^80}'.format('PROJETO DE BANCO DE DADOS 3° BIMESTRE - LOCAIS ACESSÍVEIS'))
            print('-='*62)
            infobanco = conexao.get_server_info()
            print(f'Conexão com o servidor estabelecida - Versão {infobanco}')
            comandosql = conexao.cursor()
            comandosql.execute('select database();')
            nomebanco = comandosql.fetchone()
            comandosql.close()
            print(f'O banco de dados {nomebanco} foi acessado com sucesso')
            print('-='*62)
            return True
        else:
            print("A conexão com o banco não foi realizada")
            print('-='*62)
            return False
    except Exception as erro:
        print(f'Erro detectado: {erro}')
        return False

def consultartodos():
    grid = PrettyTable(['Nomes dos Locais', 'Endereços','Tipos de Acessibilidade'])
    try:
        comandosql = conexao.cursor()
        comandosql.execute('select * from locais;')
        tabela = comandosql.fetchall()
        if len(tabela) > 0:
            for registro in tabela:
                grid.add_row([registro[1], registro[2], registro[3]])
            print(grid)
        else:
            print('Não existem locais cadastrados!')
        comandosql.close()
    except Exception as erro:
        print(f'Erro detectado: {erro}')

def consultaportipo(tipo_acessibilidade=''):
    try:
        comandosql = conexao.cursor()
        comandosql.execute(f'select * from locais where tipo_acessibilidade="{tipo_acessibilidade}";')
        tabela = comandosql.fetchall()
        if len(tabela) > 0:
            grid = PrettyTable(['Nome do Local','Endereço','Tipo de Acessibilidade'])
            for registro in tabela:
                grid.add_row([registro[1], registro[2], registro[3]])
            print('-='*62)
            print(grid)
        else:
            print('-='*62)
            print('Esse local não está cadastrado!')
        comandosql.close()
    except Exception as erro:
        print(f'Erro detectado: {erro}')

def cadastrarlocal(nome='', endereco='', tipo_acessibilidade=''):
    try:
        comandosql = conexao.cursor()
        comandosql.execute(f'select * from locais WHERE nome = "{nome}";')
        if comandosql.fetchone():
            comandosql.close()
            print('-='*62)
            return 'Já existe um local cadastrado com este nome'
        else:
            comandosql.execute(f'insert into locais(nome, endereco, tipo_acessibilidade) values("{nome}","{endereco}","{tipo_acessibilidade}") ;')
            conexao.commit()
            comandosql.close()
            return 'Local acessível cadastrado com sucesso!'
    except Exception as erro:
        print(f'Erro detectado: {erro}')
        return 'Não foi possível cadastrar este local!'

def alterartudo(nome='', novonome='', endereco='', tipo_acessibilidade=''):
    try:
        comandosql = conexao.cursor()
        comandosql.execute(f'select * from locais where nome = "{nome}"')
        if not comandosql.fetchone():
            print('-='*62)
            return 'Este local não está cadastrado'
        else:
            comandosql.execute(f'update locais set nome = "{novonome}" where nome = "{nome}";')
            comandosql.execute(f'update locais set endereco = "{endereco}" where nome = "{novonome}";')
            comandosql.execute(f'update locais set tipo_acessibilidade = "{tipo_acessibilidade}" where nome = "{novonome}";')
            conexao.commit()
            comandosql.close()
            return 'Local alterado com sucesso!'
    except Exception as erro:
        print(f'Erro detectado: {erro}')
        return 'Não foi possível alterar este local!'
    
def alterarnome(nome='', novonome=''):
    try:
        comandosql = conexao.cursor()
        comandosql.execute(f'select * from locais where nome = "{nome}"')
        if not comandosql.fetchone():
            return 'Este local não está cadastrado'
        else:
            comandosql.execute(f'update locais set nome = "{novonome}" where nome = "{nome}";')
            conexao.commit()
            comandosql.close()
            return 'Nome do local alterado com sucesso!'
    except Exception as erro:
        print(f'Erro detectado: {erro}')
        return 'Não foi possível alterar o nome deste local!'

def alterarendereco(nome='', novoendereco=''):
    try:
        comandosql = conexao.cursor()
        comandosql.execute(f'select * from locais where nome = "{nome}"')
        if not comandosql.fetchone():
            return 'Este local não está cadastrado'
        else:
            comandosql.execute(f'update locais set endereco = "{novoendereco}" where nome = "{nome}" ')
            conexao.commit()
            comandosql.close()
            return 'Endereço do local alterado com sucesso! '
    except Exception as erro:
        print(f'Erro detectado: {erro}')
        return 'Não foi possível alterar o endereço deste local!'

def alteraracessibilidade(nome='', novotipo=''):
    try:
        comandosql = conexao.cursor()
        comandosql.execute(f'select * from locais where nome = "{nome}"')
        if not comandosql.fetchone():
            return 'Este local não está cadastrado'
        else:
            comandosql.execute(f'update locais set tipo_acessibilidade = "{novotipo}" where nome = "{nome}"')
            conexao.commit()
            comandosql.close()
            return 'Tipo de acessibilidade do local alterado com sucesso!'
    except Exception as erro:
        print(f'Erro detectado: {erro}')
        return 'Não foi possível alterar o tipo de acessibilidade deste local'

def deletarlocal(nome=''):
    try:
        comandosql = conexao.cursor()
        comandosql.execute(f'select * from locais where nome = "{nome}";')
        if not comandosql.fetchone():
            return 'Este local não está cadastrado'
        else:
            comandosql.execute(f'delete from locais where nome = "{nome}";')
            conexao.commit()
            comandosql.close()
            return 'Local excluído com sucesso!'
    except Exception as erro:
        print(f'Erro detectado: {erro}')
        return 'Não foi possível excluir este local!'
    
####################################### MÓDULO PRINCIPAL DO PROGRAMA ######################################

if ativabanco() == True:
    print('Deseja entrar no módulo de locais?:')
    print('- [Sim]')
    print('- [Não]')
    print('-='*62)
    resp = input().lower().strip()
    
    while resp not in ['não','nao','sim']:
        print('-='*62)
        print("Entrada inválida, insira uma opção válida")
        print('Deseja entrar no módulo de Locais?')
        print('- [Sim]')
        print('- [Não]')
        print('-='*62)
        resp = input().lower().strip()
        
    if resp == 'sim':
        while resp != '6':
            print('-='*62)
            print('[1] - Consultar todos os locais')
            print('[2] - Consultar um local específico')
            print('[3] - Cadastrar um novo local')
            print('[4] - Alterar um local cadastrado')
            print('[5] - Excluir um local cadastrado')
            print('[6] - Sair')
            print('-='*62)
            resp = input().strip()
            
            while resp not in ['1', '2', '3', '4', '5', '6']:
                print('-='*62)
                print('Opção inválida inserida, selecione uma opção válida')
                resp = input().strip()
            print('-='*62)
            
            if resp == '1':
                consultartodos()
            
            if resp == '2':
                print("Insira o tipo de acessibilidade do local que deseja consultar:")
                print('-='*62)
                tipo_acessibilidade = input().strip()
                consultaportipo(tipo_acessibilidade)
                
            if resp == '3':
                print("Insira o nome do local que deseja cadastrar:")
                print('-='*62)
                nome = input().strip()
                print('-='*62)  
                print("Insira o endereço do local")
                print('-='*62)
                endereco = input().strip()
                print('-='*62)
                print("Insira o tipo de acessibilidade do local")
                print('-='*62)
                tipo_acessibilidade = input().strip()
                print('-='*62)
                mensagem = cadastrarlocal(nome, endereco, tipo_acessibilidade)
                print(mensagem)

            if resp == '4':
                print('[1] - Alterar todos os dados de um local')
                print('[2] - Alterar o nome de um local')
                print('[3] - Alterar o endereco de um local')
                print('[4] - Alterar o tipo de acessibilidade de um local')
                print('-='*62)
                resp = input()
                print('-='*62)
                
                if resp == '1':
                    print("Insira o nome do local que deseja alterar:")
                    print('-='*62)
                    nome = input().strip()
                    print('-='*62)
                    print("Insira o novo nome do local selecionado:")
                    print('-='*62)
                    novonome = input().strip()
                    print('-='*62)
                    print("Insira o novo endereço do local:")
                    print('-='*62)
                    endereco = input().strip()
                    print('-='*62)
                    print("Insira o novo tipo de acessibilidade do local:")
                    print('-='*62)
                    tipo_acessibilidade = input().strip()
                    print('-='*62)
                    mensagem = alterartudo(nome, novonome, endereco, tipo_acessibilidade)
                    print(mensagem)
                
                if resp == '2':
                    print("Insira o nome do local que deseja alterar:")
                    print('-='*62)
                    nome = input().strip()
                    print('-='*62)
                    print("Insira o novo nome do local:")
                    print('-='*62)
                    novonome = input().strip()
                    print('-='*62)
                    mensagem = alterarnome(nome, novonome)
                    print(mensagem)
                
                if resp == '3':
                    print("Insira o nome do local que deseja alterar:")
                    print('-='*62)
                    nome = input().strip()
                    print('-='*62)
                    print("Insira o novo endereço do local:")
                    print('-='*62)
                    novoendereco = input().strip()
                    print('-='*62)
                    mensagem = alterarendereco(nome, novoendereco)
                    print(mensagem)
                
                if resp == '4':
                    print("Insira o nome do local que deseja alterar:")
                    print('-='*62)
                    nome = input().strip()
                    print('-='*62)
                    print("Insira o novo tipo de acessibilidade do local:")
                    print('-='*62)
                    novotipo = input().strip()
                    print('-='*62)
                    mensagem = alteraracessibilidade(nome, novotipo)
                    print(mensagem)
                
            if resp == '5':
                print("Insira o nome do local que deseja deletar:")
                print('-='*62)
                nome = input().strip()
                print('-='*62)
                mensagem = deletarlocal(nome)
                print(mensagem)
                
            if resp == '6':
                print("Fim de execução do programa!")
                print('-='*62)
                conexao.close()
                break
    else:
        print('-='*62)
        print("Fim de execução do programa!")
        print('-='*62)
        conexao.close()
else:
    print('Fim de execução do progama, um problema de conexão com o banco de dados foi detectado.')