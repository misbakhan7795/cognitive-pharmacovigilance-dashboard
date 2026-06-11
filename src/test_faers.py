import pandas as pd

demo = pd.read_csv(
    "data/faers/ASCII/DEMO25Q4.txt",
    sep="$",
    encoding="latin1",
    low_memory=False
)

print(demo.head())
print()
print("Rows:", len(demo))