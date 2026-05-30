import pandas as pd

FILE_PATH = "data/HLTY-Rooted.xlsx"


def get_creator(message):

    df = pd.read_excel(
        FILE_PATH,
        sheet_name="creator_briefs"
    )

    message = (
        message.lower()
        .replace(" ", "")
    )

    for _, row in df.iterrows():

        creator_name = (
            str(row["name"])
            .lower()
            .replace(" ", "")
        )

        if creator_name in message:
            return row.to_dict()

    return None