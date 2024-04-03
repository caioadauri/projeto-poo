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


