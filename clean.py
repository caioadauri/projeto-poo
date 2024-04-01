import pandas as pd

df = pd.read_csv('./three_columns.csv')

# renomeando as colunas
df.rename(columns = {'Índice FipeZAP': 'Data'}, inplace=True)
df.rename(columns = {'Unnamed: 0': 'Índice FipeZAP'}, inplace=True)
df.rename(columns = {'Imóveis residenciais': 'Total'}, inplace=True)

# # limpando dados inutilizados da tabela Data e removendo o '00:00:00'
df['Data'] = df['Data'].str.replace('Data', 'None')
df['Data'] = df['Data'].str.replace(' 00:00:00', '')

# limpando ultimas linhas
df = df.iloc[:197]

# # limpando primeiras 3 linhas e resetando indice
df = df.iloc[3:]
df.reset_index(drop=True, inplace=True)
df['Índice FipeZAP'] = range(len(df))

# convertendo a data
df['Data'] = pd.to_datetime(df['Data']).dt.date

# arredondando o Total
df['Total'] = df['Total'].round(2)

# salvar o que foi feito no arquivo
df.to_csv('./three_columns.csv', index=False)

print(df.dtypes)
mostrar = df.iloc[:31]
display(mostrar)