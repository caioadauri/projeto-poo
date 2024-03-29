import pandas as pd
import os

# separar cada aba do excel
excel_file = pd.ExcelFile('fipezap-serieshistoricas.xlsx')

for sheet_name in excel_file.sheet_names:
    df = excel_file.parse(sheet_name)
    df.to_csv(f'{sheet_name}.csv', index=False)

# remover abas que não iremos trabalhar
files_to_keep = ['main.ipynb', 'Índice FipeZAP.csv']
all_files = os.listdir()

for file in all_files:
    if file not in files_to_keep:
        try:
            os.remove(file)
            print(f"{file} arquivo removido.")
        except PermissionError:
            print(f"Permissão negada: {file}.")

# copiar a planilha original para manipular
original_df = pd.read_csv('Índice FipeZAP.csv')
save_copy = original_df.to_csv('copy_indiceZAP.csv')
df = pd.read_csv('copy_indiceZAP.csv')

# remover tabelas desnecessarias
df_remove = df.loc[:, ~df.columns.str.contains('^Unnamed')]
three_columns = df_remove.iloc[:, :2]
save_df = three_columns.to_csv('modified_indiceZAP.csv')
