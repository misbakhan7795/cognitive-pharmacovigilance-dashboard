import pandas as pd

DATA_PATH = "data/reviews/drugsComTrain_raw.csv"

df = pd.read_csv(DATA_PATH)

def get_drug_stats(drug_name):

    drug_df = df[
        df["drugName"].str.lower()
        ==
        drug_name.lower()
    ]

    if len(drug_df) == 0:
        return {
            "review_count": 0,
            "avg_rating": 0,
            "sample_review": ""
        }

    return {
        "review_count": len(drug_df),
        "avg_rating": round(
            drug_df["rating"].mean(),
            2
        ),
        "sample_review": str(
            drug_df.iloc[0]["review"]
        )
    }