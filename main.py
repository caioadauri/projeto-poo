from read import Read
from convert import Convert
from view import FileCSV
from graph import Graph
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

retorno_tabela = retorno.soma_por_ano()

mediana = retorno.mediana()

desvio = retorno.desvio_padrao_ano()

primeiro_quartil = retorno.primeiro_quartil()

terceiro_quartil = retorno.terceiro_quartil()

coeficiente_variacao = retorno.coeficiente_variacao()

graph = Graph()

# graph.plot_media_ano()

# print(csv.dataframe)
# resumo = retorno.resumo()
# print('---------------------------')

print(f'Média: {media}')
# print(f'Soma: {retorno_tabela}')
# print(f'Mediana: {mediana}')
# print(f'Desvio: {desvio}')
# print(f'Primeiro Quartil {primeiro_quartil}')
# print(f'Terceiro Quartil { terceiro_quartil}')
print(f'Coeficiente de Variação: {coeficiente_variacao}')
print(csv.dataframe)

csv.dataframe.plot(kind='box', figsize=(15,5), vert=False, title='Boxplot')

# print(retorno.dataframe['Total'])






# x = retorno.dataframe['Data']
# y = retorno.dataframe.index
# plt.plot(x, y, 'r--')
# plt.xlabel('Data')
# plt.ylabel('Total')
# plt.title('Distribuição normal dos índices')
# plt.show()


# import pandas as pd
# df = pd.read_csv('fipezap.csv', header=None).rename(columns={0:'Data', 1: 'Valores'}).set_index('Data')
# df.index = pd.to_datetime(df.index, format='mixed').date
# df.plot(figsize=(15,10))