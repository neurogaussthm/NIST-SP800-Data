import os
import pandas as pd

df = pd.read_parquet("../by-heading-mteb-parquet/SP800-ALL.parquet")
print(df.head())
