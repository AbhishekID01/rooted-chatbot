import pandas as pd
import re

FILE_PATH = "data/HLTY-Rooted.xlsx"


def get_slang(message):

    df = pd.read_excel(
        FILE_PATH,
        sheet_name="slang_decoder"
    )

    words = re.findall(
        r"\b\w+\b",
        message.lower()
    )

    for _, row in df.iterrows():

        slang = str(
            row["slang"]
        ).lower().strip()

        if slang in words:
            return row.to_dict()

    return None