from openpyxl import load_workbook
import pandas as pd
from extract_vendas import extrair_vendas
from extract_produtos import extrair_produtos

def mesclar_tabelas():
    vendas=extrair_vendas()
    produtos=extrair_produtos()

    df_total=vendas.merge(produtos,on="ID_Produto",how="left")

    return df_total

if __name__=="__main__":
    df_final=mesclar_tabelas()
    print(df_final)
    print("\nTotal de linhas:", len(df_final))
    # Select * from Vendas inner join Produtos ON Vendas.id_produto=Produtos.id_produto