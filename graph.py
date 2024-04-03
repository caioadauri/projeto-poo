from read import Read
from convert import Convert
from view import FileCSV
import numpy as np
import matplotlib.pyplot as plt

retorno = FileCSV('fipezap.csv')
media = retorno.media()

class Graph():
  def plot_media_ano(self):
    media_ano_fig = retorno.media()
    plt.plot(media_ano_fig.index, media_ano_fig.values, marker='o', linestyle='-')
    plt.title('Curva Índice vs Tempo')
    plt.xlabel('Ano')
    plt.ylabel('Média do Índice por Ano')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

  def boxplot(self):
    retorno.dataframe.plot(kind='box', figsize=(15,5), vert=False, title='Boxplot')


box = Graph()

box.boxplot()
