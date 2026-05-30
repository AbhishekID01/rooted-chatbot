import pandas as pd

FILE_PATH = "data/HLTY-Rooted.xlsx"


def get_slang(slang_word):
    df = pd.read_excel(FILE_PATH, sheet_name="slang_decoder")

    result = df[
        df["slang"].astype(str).str.lower() == slang_word.lower()
    ]

    if result.empty:
        return None

    return result.iloc[0].to_dict()