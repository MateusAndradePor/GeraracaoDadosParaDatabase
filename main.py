import dataGenerate
import dataConvert
import fileMove
import dataMySQL

# Script gera dados de funcionários e clientes em tabelas, converte os dados e importa para uma database.
# Será criada a seguinte DataBase: loja_m
# Este script funciona apenas para Workbench, outras IDE's requerem adaptação completa

if __name__ == '__main__':
    # Gerar funcionários:
    dataGenerate.gerar_funcionarios(1000)

    # Gerar clientes:
    dataGenerate.gerar_clientes(1000)

    # Gerar Tabelas:
    dataConvert.csv_to_json('funcionarios.csv', 'funcionarios')
    dataConvert.csv_to_json('clientes.csv', 'clientes')

    # Move o arquivo para a pasta de controle do MySQL (Workbench apenas)
    fileMove.move_json('C:/ProgramData/MySQL/MySQL Server 8.0', 'funcionarios')
    fileMove.move_json('C:/ProgramData/MySQL/MySQL Server 8.0', 'clientes')

    # Passar todos os dados para uma Database (Workbench apenas):
    dataMySQL.conexao_mysql('localhost', 'root', 'pwd')
