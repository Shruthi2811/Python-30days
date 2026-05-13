#* Process a larger CSV in chunks
#* Identify outliers using a simple rule
#* Remove or cap outliers
import pandas as pd
def play_with_csv(file):
    chunks = []
    for chunk in pd.read_csv(file, chunksize=4):
        chunks.append(chunk)

    df = pd.concat(chunks, ignore_index=True)
    # Step 2: Calculate IQR bounds for the 'amount' column
    Q1 = df["amount"].quantile(0.25)
    Q3 = df["amount"].quantile(0.75)
    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # Step 3A: Identify outliers
    outliers = df[(df["amount"] < lower_bound) | (df["amount"] > upper_bound)]
    print("Outliers:")
    print(outliers)

    # Step 3B Option 1: Remove outliers
    df_removed = df[(df["amount"] >= lower_bound) & (df["amount"] <= upper_bound)]

    print("\nData after removing outliers:")
    print(df_removed)

    # Step 3C Option 2: Cap outliers
    df_capped = df.copy()
    df_capped["amount"] = df_capped["amount"].clip(lower=lower_bound, upper=upper_bound)

    print("\nData after capping outliers:")
    print(df_capped)

play_with_csv("sales.csv")