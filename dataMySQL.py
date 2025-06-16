import mysql.connector

# Criando conexão e executando uma query de forma direta:
def conexao_mysql(host, user, password):
    # Criar Conexão:
    try:
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
        )
        print('Conexão MySQL executada com sucesso.')
    except mysql.connector.Error as err:
        print(f'Erro de conexão MySQL: {err}')

    cursor = conn.cursor()

    # Executando o script SQL:
    # Lê o script SQL inteiro
    with open('dadosLojaM.sql', encoding='utf8') as f:
        script = f.read()

    # Divide por ponto e vírgula, assumindo que cada comando termina com ";"
    comandos = [cmd.strip() for cmd in script.split(';') if cmd.strip()]

    for comando in comandos:
        try:
            cursor.execute(comando)
        except Exception as e:
            print("Erro ao executar comando:", comando)
            print("Erro:", e)

    # Fecha a conexão:
    conn.commit()
    cursor.close()
    conn.close()
