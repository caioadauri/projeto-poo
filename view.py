import pandas as pd
import numpy as np
import matplotlib as plt

class FileCSV():
  def __init__(self, file):
    self.file = file
    self.dataframe = pd.read_csv(file)
    self.data = self.dataframe['Data'] = pd.to_datetime(self.dataframe['Data'])


  
  def media(self):
    media = self.dataframe.groupby(self.dataframe['Data'])['Total'].mean()

    return media.round(2)
  
  def soma_por_ano(self):
    soma = self.dataframe.groupby(self.dataframe['Data'].dt.year)['Total'].describe()

    return soma
  
  def mediana(self):
    soma_por_ano = self.soma_por_ano()
    mediana_por_ano = {}
    for ano in soma_por_ano.index:
      mediana_por_ano[ano] = soma_por_ano.loc[ano]['50%']

    return mediana_por_ano
  
  def primeiro_quartil(self):
    quartil_por_ano = self.soma_por_ano()
    primeiro_quartil_por_ano = {}
    for ano in quartil_por_ano.index:
      primeiro_quartil_por_ano[ano] = quartil_por_ano.loc[ano]['25%']
    return primeiro_quartil_por_ano
  
  def terceiro_quartil(self):
    quartil_por_ano = self.soma_por_ano()
    terceiro_quartil_por_ano = {}
    for ano in quartil_por_ano.index:
      terceiro_quartil_por_ano[ano] = quartil_por_ano.loc[ano]['75%']
    return terceiro_quartil_por_ano
  
  def desvio_padrao_ano(self):
    desvio_padro_por_ano = self.dataframe.groupby(self.dataframe['Data'].dt.year)['Total'].std()

    return desvio_padro_por_ano
  
  def coeficiente_variacao(self):
    media_por_ano = self.media()
    desvio_padrao_ano = self.desvio_padrao_ano()
    coeficiente_variacao = {}
    for ano in media_por_ano.keys():
      cv = (desvio_padrao_ano[ano] / media_por_ano[ano]) * 100
      coeficiente_variacao[ano] = cv 

    return coeficiente_variacao
  
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
  



