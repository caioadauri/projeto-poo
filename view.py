import pandas as pd

class FileCSV():
  def __init__(self, file):
    self.file = file
    self.dataframe = pd.read_csv(file)
    self.data = self.dataframe['Data'] = pd.to_datetime(self.dataframe['Data'])

  
  def media(self):
    media = self.dataframe['Total'].mean()

    return media
  
  def soma(self):
    soma = self.dataframe['Total'].count()

    return soma
  
  def mediana(self):
    mediana = self.dataframe['Total'].median()

    return mediana
  
  def coeficiente_variacao(self):
    coeficiente_variacao = self.dataframe['Total'].std() / self.dataframe['Total'].mean() * 100

    return coeficiente_variacao
  
  def resumo(self):
    resumo = self.dataframe['Total'].describe()

    return resumo


