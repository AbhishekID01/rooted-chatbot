import pandas as pd

FILE_PATH = "data/HLTY-Rooted.xlsx"


def get_faq(user_question):

    df = pd.read_excel(
        FILE_PATH,
        sheet_name="FAQ"
    )

    result = df[
        df["question"]
        .astype(str)
        .str.lower()
        .str.contains(user_question.lower(), na=False)
    ]

    if result.empty:
        return None

    return result.iloc[0].to_dict()