# Importando SQLITE
import sqlite3 as lite

# Criando conexao
conexao = lite.connect("dados.db")


# CRUD

    # Inserindo dados
def inserir_form(i):
    with conexao:
        cursor = conexao.cursor()
        query = "INSERT INTO inventario(nome, local, descricao, marca, data_da_compra, valor_da_compra, serie, imagem) VALUES(?,?,?,?,?,?,?,?)"
        cursor.execute(query,i)


# Atualizando dados
def atualizar_form(i):
    with conexao:
        cursor = conexao.cursor()
        query = "UPDATE inventario SET nome=?, local=?, descricao=?, marca=?, data_da_compra=?, valor_da_compra=?, serie=?, imagem=? WHERE id=?"
        cursor.execute(query, i)

# Deletar dados
def deletar_form(i):
    with conexao:
        cursor = conexao.cursor()
        query = "DELETE FROM inventario WHERE id=?"
        cursor.execute(query,i)


# Ver dados
def ver_form():
    ver_dados = []
    with conexao:
        cursor = conexao.cursor()
        query = "SELECT * FROM inventario"
        cursor.execute(query)

        linhas = cursor.fetchall()
        for linha in linhas:
            ver_dados.append(linha)
    return ver_dados

# Ver dados individual
def ver_item(id):
    ver_dados_unitarios = []
    with conexao:
        cursor = conexao.cursor()
        query = "SELECT * FROM inventario WHERE id=?"
        cursor.execute(query, id)

        linhas = cursor.fetchall()
        for linha in linhas:
            ver_dados_unitarios.append(linha)

    return ver_dados_unitarios