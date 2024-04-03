from read import Read
from convert import Convert
from view import FileCSV
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

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
    df = retorno.dataframe['Total'].tolist()
    plt.boxplot(df)
    plt.xlabel('Índices')
    plt.title('Boxplot dos Indices')
    plt.grid()
    plt.show()

  def plot_distribuicao_normal(self):
    indices = retorno.dataframe['Total']
    plt.hist(indices, bins=25, density=True, alpha=0.6, color='b')
    mu, sigma = indices.mean(), indices.std()
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mu, sigma)
    plt.plot(x, p, 'k', linewidth=2)
    plt.xlabel('Índices')
    plt.ylabel('Frequencia')
    plt.title('Distribuição Normal dos Índices')
    plt.show()

    


