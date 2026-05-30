import pandas as pd

FILE_PATH = "data/HLTY-Rooted.xlsx"


def get_faq(message):

    df = pd.read_excel(
        FILE_PATH,
        sheet_name="FAQ"
    )

    message = message.lower()

    for _, row in df.iterrows():

        question = str(
            row["question"]
        ).lower()

        words = question.split()

        matches = sum(
            1 for word in words
            if word in message
        )

        if matches >= 3:
            return row.to_dict()

    return None