import pandas as pd

df = pd.read_excel('./zap.xlsx')
df.to_csv('FIPE.csv', index=False)

fileCSV = pd.read_csv('./FIPE.csv')
print(fileCSV)


