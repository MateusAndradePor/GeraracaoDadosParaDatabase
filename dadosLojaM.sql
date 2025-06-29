-- Verificar os caminhos e atualizar de acordo com o caminho do Workbench
-- DROP DATABASE IF EXISTS loja_m;
CREATE DATABASE IF NOT EXISTS loja_m;
USE loja_m;

GRANT FILE ON *.* TO 'root'@'localhost';

CREATE TABLE IF NOT EXISTS funcionarios (
  id_funcionario INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(100),
  email VARCHAR(100),
  cargo VARCHAR(50),
  idade INT,
  loja INT,
  estado VARCHAR(50),
  vendas_totais INT,
  vendas_produto_1 INT,
  vendas_produto_2 INT,
  vendas_produto_3 INT
);

CREATE TABLE IF NOT EXISTS clientes (
  id_cliente INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(100),
  cpf VARCHAR(14),
  email VARCHAR(100),
  telefone VARCHAR(55),
  estado VARCHAR(55),
  compras INT
);

-- Tabela JSON para funcionários
CREATE TABLE IF NOT EXISTS json_import_f (
  data JSON
);
-- Tabela JSON para clientes
CREATE TABLE IF NOT EXISTS json_import_c (
  data JSON
);

INSERT INTO json_import_f (data)
VALUES (
  CAST(LOAD_FILE('C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\funcionarios.json') AS CHAR CHARACTER SET utf8mb4)
);

INSERT INTO json_import_c (data)
VALUES (
  CAST(LOAD_FILE('C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\clientes.json') AS CHAR CHARACTER SET utf8mb4)
);

-- Inserindo dados dos funcionários:
INSERT INTO funcionarios (
  nome,
  email,
  cargo,
  idade,
  loja,
  estado,
  vendas_totais,
  vendas_produto_1,
  vendas_produto_2,
  vendas_produto_3
)
SELECT
  jt.Nome,
  jt.Email,
  jt.Cargo,
  jt.Idade,
  jt.Loja,
  jt.Estado,
  jt.`Vendas Totais`,
  jt.`Vendas - Produto 1`,
  jt.`Vendas - Produto 2`,
  jt.`Vendas - Produto 3`
FROM json_import_f,
JSON_TABLE(
  data,
  '$[*]' COLUMNS (
    Nome VARCHAR(100) PATH '$.Nome',
    Email VARCHAR(100) PATH '$.Email',
    Cargo VARCHAR(50) PATH '$.Cargo',
    Idade INT PATH '$.Idade',
    Loja INT PATH '$.Loja',
    Estado VARCHAR(50) PATH '$.Estado',
    `Vendas Totais` INT PATH '$."Vendas Totais"',
    `Vendas - Produto 1` INT PATH '$."Vendas - Produto 1"',
    `Vendas - Produto 2` INT PATH '$."Vendas - Produto 2"',
    `Vendas - Produto 3` INT PATH '$."Vendas - Produto 3"'
  )
) AS jt;

-- Inserindo dados dos clientes:
INSERT INTO clientes (
	nome,
    cpf,
    email,
    telefone,
    estado,
    compras
)
SELECT
	jt.Nome,
    jt.CPF,
    jt.Email,
    jt.Telefone,
    jt.Estado,
    jt.Compra
FROM json_import_c,
JSON_TABLE (
	data,
	'$[*]' COLUMNS (
		Nome VARCHAR(100) PATH '$.Nome',
        CPF VARCHAR(14) PATH '$.CPF',
        Email VARCHAR(100) PATH '$.Email',
        Telefone VARCHAR(55) PATH '$.Telefone',
        Estado VARCHAR(55) PATH '$.Estado',
        Compra INT PATH '$.Compra'        
    )
) AS jt;
	

-- Teste das tabelas:/
-- SELECT * FROM funcionarios LIMIT 10;
-- SELECT * FROM clientes LIMIT 10;