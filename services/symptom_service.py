import pandas as pd

FILE_PATH = "data/HLTY-Rooted.xlsx"


def get_symptom(message):

    df = pd.read_excel(
        FILE_PATH,
        sheet_name="symptom_lookup"
    )

    message = (
        message.lower()
        .replace(" ", "")
    )

    for _, row in df.iterrows():

        symptom = (
            str(row["symptom"])
            .lower()
            .replace(" ", "")
        )

        if symptom in message:
            return row.to_dict()

    return None