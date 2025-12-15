import pandas as pd


def extract_iqvia(path):
    """
    Lê o arquivo de vendas IQVIA e retorna um DataFrame
    """
    df = pd.read_csv(path)
    return df


def extract_filial_brick(path):
    """
    Lê o arquivo de relação filial x brick e retorna um DataFrame
    """
    df = pd.read_csv(path)
    return df
