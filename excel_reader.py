import pandas as pd


def read_excel_as_list(path: str) -> list[list[str]]:
    """
    Читает Excel-файл и возвращает список строк.
    Все значения приводятся к строкам.
    """
    df = pd.read_excel(path)
    df = df.fillna("")
    return df.astype(str).values.tolist()