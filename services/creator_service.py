import pandas as pd
from rapidfuzz import fuzz

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

    best_score = 0
    best_row = None

    for _, row in df.iterrows():

        creator_name = (
            str(row["name"])
            .lower()
            .replace(" ", "")
        )

        score = fuzz.partial_ratio(
            message,
            creator_name
        )

        if score > best_score:
            best_score = score
            best_row = row

    if best_row is not None:

        print(
            "CREATOR BEST SCORE:",
            best_score
        )

        print(
            "CREATOR MATCH:",
            best_row["name"]
        )

    if best_score >= 80:

        return {
            "score": best_score,
            "data": best_row.to_dict()
        }

    return None