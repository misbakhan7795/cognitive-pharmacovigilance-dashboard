# src/test_faers_columns.py

import pandas as pd

drug = pd.read_csv(
    "data/faers/ASCII/DRUG25Q4.txt",
    sep="$",
    encoding="latin1",
    low_memory=False
)

reac = pd.read_csv(
    "data/faers/ASCII/REAC25Q4.txt",
    sep="$",
    encoding="latin1",
    low_memory=False
)

print("\nDRUG COLUMNS")
print(drug.columns.tolist())

print("\nREAC COLUMNS")
print(reac.columns.tolist())