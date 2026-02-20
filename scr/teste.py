import pandas as pd

df=pd.ExcelFile("../data/Controle_Financeiro_Blocos_Concreto.xlsx")

print(df.sheet_names)