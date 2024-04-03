from read import Read
from convert import Convert
from view import FileCSV
import numpy as np
import matplotlib.pyplot as plt

arquivo = 'fipezap.xlsx'
aba = 'Índice FipeZAP'
coluna = 'B:C'
ignorar_linhas = 3
maximo_linhas = 194
engine = 'openpyxl'

result = Read(arquivo, aba, coluna, ignorar_linhas, maximo_linhas, engine)

csv = Convert(result.dataframe, 'fipezap.csv')

retorno = FileCSV('fipezap.csv')

media = retorno.media()

soma = retorno.soma_por_ano()

# mediana = retorno.mediana()

# coeficiente_variacao = retorno.coeficiente_variacao()


# print(csv.dataframe)
# resumo = retorno.resumo()
# print('---------------------------')
# print(f'Coeficiente de Variação: {coeficiente_variacao}')
print(f'Média: {media}')
print(f'Soma: {soma}')
# print(f'Mediana: {mediana}')

# print(retorno.dataframe['Total'])

# x = retorno.dataframe['Data']
# y = retorno.dataframe['Total'].tolist()
# plt.bar(x, y, color='red')
# plt.xlabel('Data')
# plt.ylabel('Total')
# plt.title('Distribuição normal dos índices')
# plt.show()


# import pandas as pd
# df = pd.read_csv('fipezap.csv', header=None).rename(columns={0:'Data', 1: 'Valores'}).set_index('Data')
# df.index = pd.to_datetime(df.index, format='mixed').date
# df.plot(figsize=(15,10))