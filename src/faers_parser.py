import pandas as pd

def load_faers():

    demo = pd.read_csv(
    "data/faers/ASCII/DEMO25Q4.txt",
    sep="$",
    encoding="latin1",
    low_memory=False
)

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

    return demo, drug, reac