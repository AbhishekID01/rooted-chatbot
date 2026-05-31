import pandas as pd

FILE_PATH = "data/HLTY-Rooted.xlsx"


def get_tough_topic(message):

    df = pd.read_excel(
        FILE_PATH,
        sheet_name="tough_topics"
    )

    result = df[
        df.astype(str)
        .apply(
            lambda row: row.str.lower().str.contains(
                message.lower(),
                na=False
            ).any(),
            axis=1
        )
    ]

    if result.empty:
        return None

    return {
        "score": 100,
        "data": result.iloc[0].to_dict()
    }