import pandas as pd

# Lendo o CSV e passando para JSON:
def csv_to_json(path, filename):
    # Ler arquivo:
    df = pd.read_csv(path)
    print(f'Dados de {filename}.csv convertidos para JSON')

    # Escrever em JSON:
    df.to_json(f'{filename}.json', orient='records', indent=False)

# Lendo xlsx e passando para CSV:
def xlsx_to_csv(path, filename):
    df = pd.read_excel(path)
    print(f'Dados de {filename}.xlsx convertidos para CSV')

    #Escrever em CSV:
    df.to_csv(f'{filename}.csv', index=False)
