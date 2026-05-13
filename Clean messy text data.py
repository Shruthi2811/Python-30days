#Clean messy text data
#    * lowercase
#    * remove punctuation
#   * trim spaces
#   * standardize category names

import pandas as pd
import string

def cleandata(data):
    df=pd.DataFrame(data)
    # Convert to lowercase and trim spaces
    df["product_name"] = df["product_name"].str.lower().str.strip()
    df["category"] = df["category"].str.lower().str.strip()

    # Remove punctuation from product_name
    df["product_name"] = df["product_name"].str.translate(
        str.maketrans("", "", string.punctuation)
    )

    # Standardize category names
    df["category"] = df["category"].str.replace("-", " ", regex=False)
    df["category"] = df["category"].str.strip()

    return df


data = {
    "product_name": ["  Laptop! ", "Smart-Phone ", " blender ", "Vacuum Cleaner.", " Headphones, "],
    "category": [" Electronics ", "ELECTRONICS", "home-appliances", " Home Appliances ", " electronics"]
}
df=cleandata(data)
print(df)