import sqlite3


# Função para recuperar informações do banco de dados
def retrieve_data_from_db():
    try:
        # Conecte-se ao banco de dados SQLite3
        conn = sqlite3.connect("meu_banco_de_dados.db")
        cursor = conn.cursor()

        # Execute uma consulta SQL para recuperar todos os dados
        cursor.execute("SELECT * FROM dados_monitoramento")

        # Recupere todos os resultados da consulta
        data = cursor.fetchall()

        if not data:
            print("Nenhum dado encontrado na tabela.")
        else:
            # Imprima todos os dados
            print("Registros na tabela dados_monitoramento:")
            for row in data:
                print(
                    f"ID: {row[0]}, CPU: {row[1]}, Memória: {row[2]}, Disco: {row[3]}, Timestamp: {row[4]}"
                )

    except sqlite3.Error as e:
        print(f"Erro ao recuperar dados do banco de dados: {e}")

    finally:
        # Feche a conexão com o banco de dados
        conn.close()


# Função para excluir um registro pelo ID
def delete_data_by_id(id_to_delete):
    try:
        # Conecte-se ao banco de dados SQLite3
        conn = sqlite3.connect("meu_banco_de_dados.db")
        cursor = conn.cursor()

        # Execute uma consulta SQL para excluir o registro com base no ID
        cursor.execute("DELETE FROM dados_monitoramento WHERE id = ?", (id_to_delete,))

        # Faça commit para salvar as alterações
        conn.commit()

        if cursor.rowcount > 0:
            print(f"Registro com ID {id_to_delete} foi excluído com sucesso.")
        else:
            print(f"Nenhum registro encontrado com o ID {id_to_delete}.")

    except sqlite3.Error as e:
        print(f"Erro ao excluir registro do banco de dados: {e}")

    finally:
        # Feche a conexão com o banco de dados
        conn.close()


# Função para excluir todos os registros da tabela
def delete_all_data():
    try:
        # Conecte-se ao banco de dados SQLite3
        conn = sqlite3.connect("meu_banco_de_dados.db")
        cursor = conn.cursor()

        # Execute uma consulta SQL para excluir todos os registros
        cursor.execute("DELETE FROM dados_monitoramento")

        # Faça commit para salvar as alterações
        conn.commit()

        print("Todos os registros foram excluídos com sucesso.")

    except sqlite3.Error as e:
        print(f"Erro ao excluir todos os registros: {e}")

    finally:
        # Feche a conexão com o banco de dados
        conn.close()


# Chame a função para recuperar os dados do banco de dados
retrieve_data_from_db()

# Solicite ao usuário que escolha uma opção
print("\nEscolha uma opção:")
print("1. Excluir registro por ID")
print("2. Excluir todos os registros")
choice = input("Digite o número da opção desejada (ou pressione Enter para sair): ")

if choice == "1":
    id_to_delete = input("Digite o ID do registro que deseja excluir: ")
    delete_data_by_id(id_to_delete)
elif choice == "2":
    delete_all_data()
elif choice:
    print("Opção inválida.")
