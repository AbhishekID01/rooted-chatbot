import csv
from datetime import datetime

FILE_PATH = "data/chat_logs.csv"


def log_chat(
    phone_number,
    question,
    answer
):

    with open(
        FILE_PATH,
        "a",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            datetime.now(),
            phone_number,
            question,
            answer
        ])