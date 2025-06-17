# GeraracaoDadosParaDatabase
Script que gera dados fictícios de clientes e funcionários de uma loja e, automaticamente, sobe todos os dados para uma Database.  
Script apenas para fins de estudos, útil para criar databases para análise de dados em MySQL e tratamento de dados em tabelas.  
Este script é baseado no Workbench (SQL) apenas e para funcionar em outras IDEs é necessária adaptação.  

## Requirements
Python 3.12 ou mais recente

## Dependências

```
pip3 install -r requirements.txt

```

### Descrição
1. O script gera dados de clientes e de funcionários de acordo com a quantidade especificada;  
2. Depois, estes dados são salvos em uma tabela .csv e em outra .JSON (2 tabelas para cada um);  
3. A tabela .JSON é copiada para o local correto do Workbench (este caminho deve ser especificado ao executar a função);
4. O script SQL é executado, criando uma database chamada 'loja_m' com as duas tabelas ('clientes' e 'funcionarios') importadas;
5. As conexões SQL são fechadas e o script é encerrado.

*Importante: para assegurar a conexão com o Workbench, o programa deve estar aberto durante a execução do Script.  
*Este script tem a função de estudar a integração entre Python e MySQL, a conversão de arquivos CSV para JSON e a execução de importação automática dos dados para o Workbench via Python.

### Usabilidade
1. O caminho do Workbench deve ser especificado dentro do script SQL e na chamada da função.  
Para saber o caminho correto, execute dentro do Workbench o comando:

```
SELECT @@secure_file_priv;

```

2. Usando o main.py, execute as funções com os parâmetros:

```
dataGenerate.gerar_funcionarios(quantidade_de_funcionarios)
dataGenerate.gerar_clientes(quantidade_de_clientes)

dataConvert.csv_to_json(path:'funcionarios.csv', filename:'funcionarios')
dataConvert.csv_to_json(path:'clientes.csv', filename'clientes')

# Especificar o caminho da pasta 'MySQL Server 8.0'
fileMove.move_json(serverPath:'C:/ProgramData/MySQL/MySQL Server 8.0', filename:'funcionarios')
fileMove.move_json(serverPath:'C:/ProgramData/MySQL/MySQL Server 8.0', filename:'clientes')

dataMySQL.conexao_mysql('localhost', 'root', 'pwd') # Seus dados de conexão com o Workbench
```
