import pandas as pd

class FileCSV():
  def __init__(self, file):
    self.file = file
    self.dataframe = pd.read_csv(file)
    self.data = self.dataframe['Data'] = pd.to_datetime(self.dataframe['Data'])


  
  def media(self):
    media = self.dataframe['Total'].mean()

    return media.round(2)
  
  def soma(self):
    soma = self.dataframe['Total'].sum()

    return soma.round(2)
  
  def mediana(self):
    mediana = self.dataframe['Total'].median()

    return mediana.round(2)
  
  def coeficiente_variacao(self):
    coeficiente_variacao = self.dataframe['Total'].std() / self.dataframe['Total'].mean() * 100

    return coeficiente_variacao.round(2)
  
  def resumo(self):
    resumo = self.dataframe['Total'].describe().loc[['count','mean','std','25%','50%','75%']].round(2)

    traducoes = {
    'count': 'Num Elementos',
    'mean': 'Média',
    'std': 'Desvio Padrão',
    '25%': '1° Quartil',
    '50%': 'Mediana(2° Quartil)',
    '75%': '3° Quartil'
}
    for indice, valor in resumo.items():
     print(f'{traducoes[indice]}: {valor}')

    return indice


