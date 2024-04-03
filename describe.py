import pandas as pd

def pular():
    print('\n')

df = pd.read_csv('three_columns.csv')

# calculo Coeficiente de Variação
cv = df['Total'].std() / df['Total'].mean() * 100

resumo = df['Total'].describe().loc[['count','mean','std','25%','50%','75%']].round(2)

traducoes = {
    'count': 'Num Elementos',
    'mean': 'Média',
    'std': 'Desvio Padrão',
    '25%': '1° Quartil',
    '50%': 'Mediana(2° Quartil)',
    '75%': '3° Quartil'
}

pular()
for indice, valor in resumo.items():
     print(f'{traducoes[indice]}: {valor}')
print(f'Coeficiente de Variação: {cv.round(2)}')
pular()
print('=-= tipos das colunas =-=')
for coluna in df:
    print(f'{coluna}: ',df[coluna].dtype)
pular()
print(df.iloc[:6])
 



