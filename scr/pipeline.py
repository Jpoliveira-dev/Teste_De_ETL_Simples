import pandas as pd
from openpyxl import load_workbook
from extract_produtos import extrair_produtos
from extract_vendas import extrair_vendas
from join import mesclar_tabelas
from transform import criar_dataset
from load import load

def pipeline():
    dataset=criar_dataset()
    load()

    # return pipeline()

if __name__=="__main__":
    pipeline()