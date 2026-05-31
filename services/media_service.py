import pandas as pd

FILE_PATH = "data/HLTY-Rooted.xlsx"


def get_media(message):

    df = pd.read_excel(
        FILE_PATH,
        sheet_name="media_ratings"
    )

    message = message.lower()

    for _, row in df.iterrows():

        media_name = str(
            row["name"]
        ).lower()

        if media_name in message:

            return {
                "score": 100,
                "data": row.to_dict()
            }

    return None