from faker import Faker
import random
import pandas as pd
from faker.providers import DynamicProvider

# Script para gerar tabelas correspondentes de funcionários e clientes, com números de vendas e compras compatíveis

# Provedor de estados
estados_provider = DynamicProvider(
    provider_name='estados',
    elements=[
        'Paraná',
        'São Paulo',
        'Bahia'
        # Adicionar mais estados se preciso
    ]
)

# Provedor de cargos dos funcionários:
func_provider = DynamicProvider(
    provider_name='cargos',
    elements=[
        'Vendedor A',
        'Vendedor B',
        'Vendedor C',
        'Vendedor D',
        'Transportador A',
        'Transportador B'
    ]
)

# Adiciona os provedores na biblioteca do gerador
faker = Faker('pt_BR')
faker.add_provider(func_provider)
faker.add_provider(estados_provider)

# Variáveis de controle
dados_funcionarios = []
dados_clientes = []
contr_total = []

# Gerando os funcionários com todos os dados
def gerar_funcionarios(n):
    total_vendas = 0
    for _ in range(n):
        nome = faker.name()
        cargo = faker.cargos()
        idade = random.randint(18, 65)
        loja = random.randint(1, 5)
        format_email = f'{nome.lower().replace(" ","")}@mploja{loja}'
        email = f'{format_email.replace('.', '')}.com.br'
        estado = faker.estados()
        vendas_totais = random.randint(100, 500)
        # Geração de vendas aleatórias de produtos
        produto1 = random.randint(50, 300)
        if produto1 > vendas_totais:
            produto1 = vendas_totais
        else:
            produto1 = produto1
        restante = vendas_totais - produto1
        produto2 = random.randint(0, restante)
        produto3 = restante - produto2

        funcionario = {
            'Nome': nome,
            'Email': email,
            'Cargo': cargo,
            'Idade': idade,
            'Loja': loja,
            'Estado': estado,
            'Vendas Totais': vendas_totais,
            'Vendas - Produto 1': produto1,
            'Vendas - Produto 2': produto2,
            'Vendas - Produto 3': produto3
        }
        dados_funcionarios.append(funcionario)

        # Variáveis que vão sair da função
        total_vendas = total_vendas + vendas_totais

    # Exportando valores para fora da função
    contr_total.append(total_vendas)

    print('Geração de funcionários concluída')
    df = pd.DataFrame(dados_funcionarios)
    df.to_csv('funcionarios.csv', encoding='utf-8-sig')

# Gerando os clientes com todos os dados
def gerar_clientes(n):
    total_vendas = contr_total[0]
    contr_compras = 0
    controle_vend = round(total_vendas / (n*0.5))
    for _ in range(n):
        nome = faker.name()
        cpf = faker.cpf()
        estado = faker.estado()
        format_email = f'{nome.lower().replace(" ","")}' # Formata o email corretamente
        email = f'{format_email.replace(".", "")}@email.com'
        tel = faker.phone_number()
        # Deixando o total de vendas dos funcionários e as compras dos clientes com mesmo volume
        if contr_compras >= total_vendas:
            contr_compras = total_vendas
            compras = 0
        else:
            compras = random.randint(0, controle_vend)
            contr_compras += compras
            if contr_compras > total_vendas:
                sum = contr_compras - compras
                contr_compras = total_vendas
                compras = total_vendas - sum
                print('Geração de clientes concluída.')
            elif contr_compras < total_vendas and len(dados_clientes) == n-1:
                sum = total_vendas - contr_compras
                compras = sum
                contr_compras = total_vendas
                print('Geração de clientes concluída com assimetria (vendas != compras)')

        cliente = {
            'Nome': nome,
            'CPF': cpf,
            'Email': email,
            'Telefone': tel,
            'Estado': estado,
            'Compra': compras
        }

        dados_clientes.append(cliente)
        df = pd.DataFrame(dados_clientes)
        df.to_csv('clientes.csv', encoding='utf-8-sig')

    if contr_compras != total_vendas:
        print('Erro na geração de compras dos clientes, gere novamente')

# A geração de dados pode necessitar tratamento de dados
# e.g: clientes com 0 compra realizada podem ser gerados e devem ser filtrados
