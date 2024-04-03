from read import Read
from convert import Convert


arquivo = 'fipezap.xlsx'
aba = 'Índice FipeZAP'
coluna = 'B:C'
ignorar_linhas = 3
maximo_linhas = 194
engine = 'openpyxl'

result = Read(arquivo, aba, coluna, ignorar_linhas, maximo_linhas, engine)

csv = Convert(result.dataframe, 'fipezap.csv')
