import pandas as pd
import re

FILE_PATH = "data/HLTY-Rooted.xlsx"


def get_faq(message):

    df = pd.read_excel(
        FILE_PATH,
        sheet_name="FAQ"
    )

    message = message.lower()

    message_words = set(
        re.findall(r"\b\w+\b", message)
    )

    stop_words = {
        "is", "are", "the", "a", "an",
        "to", "of", "in", "on", "for",
        "do", "does", "did", "my",
        "how", "what", "why", "when",
        "if", "i", "you", "your"
    }

    for _, row in df.iterrows():

        question = str(
            row["question"]
        ).lower()

        question_words = set(
            re.findall(r"\b\w+\b", question)
        )

        question_words = {
            word for word in question_words
            if word not in stop_words
        }

        matches = len(
            question_words.intersection(
                message_words
            )
        )

        if matches >= 3:
            return row.to_dict()

    return None