import pandas as pd
from rapidfuzz import fuzz

FILE_PATH = "data/HLTY-Rooted.xlsx"


def get_creator(message):

    df = pd.read_excel(
        FILE_PATH,
        sheet_name="creator_briefs"
    )

    message = message.lower()

    best_match = None
    best_score = 0

    for _, row in df.iterrows():

        creator_name = str(
            row["name"]
        ).lower()

        score = fuzz.partial_ratio(
            creator_name,
            message
        )

        if score > best_score:
            best_score = score
            best_match = row.to_dict()

    if best_score >= 80:
        return best_match

    return None