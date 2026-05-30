import pandas as pd

FILE_PATH = "data/HLTY-Rooted.xlsx"


def get_meme(message):

    df = pd.read_excel(
        FILE_PATH,
        sheet_name="meme_translator"
    )

    message = (
        message.lower()
        .replace(" ", "")
    )

    for _, row in df.iterrows():

        meme_phrase = (
            str(row["meme_phrase"])
            .lower()
            .replace(" ", "")
        )

        if meme_phrase in message:
            return row.to_dict()

    return None