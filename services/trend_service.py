import pandas as pd

FILE_PATH = "data/HLTY-Rooted.xlsx"


def get_trend(keyword):

    df = pd.read_excel(
        FILE_PATH,
        sheet_name="trend_issues"
    )

    result = df[
        df.astype(str)
        .apply(
            lambda row: row.str.lower().str.contains(
                keyword.lower(),
                na=False
            ).any(),
            axis=1
        )
    ]

    if result.empty:
        return None

    return result.iloc[0].to_dict()