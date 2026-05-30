import pandas as pd

FILE_PATH = "data/HLTY-Rooted.xlsx"


def get_slang(message):

    df = pd.read_excel(
        FILE_PATH,
        sheet_name="slang_decoder"
    )

    message = message.lower()

    for _, row in df.iterrows():

        slang = str(
            row["slang"]
        ).lower()

        if slang in message:
            return row.to_dict()

    return None