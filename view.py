# Importando SQLITE
import sqlite3 as lite

# Criando conexao
conexao = lite.connect("dados.db")


dados = ["Vaso", "Sala de estar", "Vaso que comprei na olx", "Bransk", "15/03/2023", "100", "001", "c:/imagens"]
# Inserindo dados
with conexao:
    cursor = conexao.cursor()
    query = "INSERT INTO inventario(nome, local, descricao, marca, data_da_compra, valor_da_compra, serie, imagem) VALUES(?,?,?,?,?,?,?,?)"
    cursor.execute(query,dados)