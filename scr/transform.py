from join import mesclar_tabelas
import pandas as pd

def criar_dataset():

    df_total = mesclar_tabelas()

    dataset = df_total.copy()

    # Garantir data
    dataset["Data"] = pd.to_datetime(dataset["Data"])

    # Tempo
    dataset["Ano"] = dataset["Data"].dt.year
    dataset["Mes"] = dataset["Data"].dt.month
    dataset["AnoMes"] = dataset["Data"].dt.to_period("M").astype(str)

    # Receita por cliente
    dataset["Receita_Cliente"] = (
        dataset.groupby("Cliente")["Receita"].transform("sum")
    )

    # Lucro por produto
    dataset["Lucro_Produto"] = (
        dataset.groupby("Nome_Produto")["Lucro"].transform("sum")
    )

    # Receita por categoria
    dataset["Receita_Categoria"] = (
        dataset.groupby("Categoria")["Receita"].transform("sum")
    )

    # Ticket por cliente
    dataset["Ticket_Cliente"] = (
        dataset.groupby("Cliente")["Receita"].transform("mean")
    )

    return dataset
    

if __name__ == "__main__":
    df = criar_dataset()
    print(df.head())