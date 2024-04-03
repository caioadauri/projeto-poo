from read import Read
from convert import Convert
from view import FileCSV


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

soma = retorno.soma()

mediana = retorno.mediana()

coeficiente_variacao = retorno.coeficiente_variacao()


print(csv.dataframe)
resumo = retorno.resumo()
print('---------------------------')
print(f'Coeficiente de Variação: {coeficiente_variacao}')
print(f'Média: {media}')
print(f'Soma: {soma}')
print(f'Mediana: {mediana}')


