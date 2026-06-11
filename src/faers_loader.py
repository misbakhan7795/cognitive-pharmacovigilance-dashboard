import pandas as pd

print("Loading DRUG file...")

drug = pd.read_csv(
    "data/faers/ASCII/DRUG25Q4.txt",
    sep="$",
    encoding="latin1",
    low_memory=False
)

print("Loading REAC file...")

reac = pd.read_csv(
    "data/faers/ASCII/REAC25Q4.txt",
    sep="$",
    encoding="latin1",
    low_memory=False
)

print("Joining tables...")

merged = pd.merge(
    drug[["primaryid", "drugname"]],
    reac[["primaryid", "pt"]],
    on="primaryid",
    how="inner"
)

print("Rows after merge:", len(merged))

# Keep only first 100k rows for capstone/demo
merged = merged.head(100000)

print("Using rows:", len(merged))

# Rename columns
merged = merged.rename(
    columns={
        "drugname": "drug",
        "pt": "reaction"
    }
)

print("Saving CSV...")

merged.to_csv(
    "data/processed/faers_records.csv",
    index=False
)

print("DONE")
print("Records saved:", len(merged))