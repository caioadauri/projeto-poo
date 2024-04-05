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

graph.plot_media_ano()
graph.boxplot()
graph.plot_distribuicao_normal()

print(f'Média: {media}')
print(f'Soma: {retorno_tabela}')
print(f'Mediana: {mediana}')
print(f'Desvio: {desvio}')
print(f'Primeiro Quartil {primeiro_quartil}')
print(f'Terceiro Quartil { terceiro_quartil}')
print(f'Coeficiente de Variação: {coeficiente_variacao}')

