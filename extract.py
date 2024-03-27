import pandas as pd


class TabelaFipe():
    def __init__(self) -> None:
        self.df=pd.read_excel('./zap.xlsx')
        self.df.to_csv('FIPE.csv', index=False)
        self.fileCSV = pd.read_csv('./FIPE.csv')

    def qtdElementos(self):
        return len(self.df)
    
    def separacaocolumns(self):
        df = pd.DataFrame(eval('./FIPE.csv'))
        duas_colunas = df[['Data', 'Total']]
        return duas_colunas

        


tabela = TabelaFipe()
print("Quantidade de elementos:", tabela.qtdElementos())
print("Coluna data: ", tabela.separacaocolumns())


