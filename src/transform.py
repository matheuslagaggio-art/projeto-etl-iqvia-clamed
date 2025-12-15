def transform_iqvia(df):
    """
    Realiza limpeza e transformação dos dados IQVIA
    """
    # padroniza nomes das colunas
    df.columns = (
        df.columns
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
    )

    # converte EAN para string
    df["ean"] = df["ean"].astype(str)

    # trata valores nulos
    df = df.fillna(0)

    # cria métricas pedidas
    df["vol_total_mercado"] = (
        df["vol_pp"]
        + df["vol_concorrente_rede"]
        + df["vol_concorrente_indep"]
    )

    df["participacao_clamed"] = (
        df["vol_pp"] / df["vol_total_mercado"]
    )

    # remove duplicatas
    df = df.drop_duplicates()

    return df
