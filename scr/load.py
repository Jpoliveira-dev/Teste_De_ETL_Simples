from transform import criar_dataset
import pandas as pd
from openpyxl import load_workbook

def load():
    dataset=criar_dataset()
    dataset.to_csv("../output/dataset.csv",index=False)