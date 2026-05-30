import pandas as pd

file_path = "data/HLTY-Rooted.xlsx"

excel_file = pd.ExcelFile(file_path)

print("\n=== SHEETS FOUND ===\n")

for sheet in excel_file.sheet_names:
    print(sheet)