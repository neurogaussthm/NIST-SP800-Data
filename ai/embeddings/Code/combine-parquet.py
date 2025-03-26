import os
import pandas as pd

base_dir = ".."

for method_dir in os.listdir(base_dir):
    method_path = os.path.join(base_dir, method_dir)
    if not os.path.isdir(method_path) or method_dir == "Code" or "numpy" in method_dir:
        continue
    all_dfs = []
    for filename in os.listdir(method_path):
        if filename.endswith(".parquet"):
            path = os.path.join(method_path, filename)
            df = pd.read_parquet(path)
            df["source"] = filename.split('_')[0]
            all_dfs.append(df)
    combined_df = pd.concat(all_dfs, ignore_index=True)
    combined_df.to_parquet(os.path.join(method_path, "SP800-ALL.parquet"))
    print(f"Combined {len(all_dfs)} files into {len(combined_df)} rows at {os.path.join(method_path, 'SP800-ALL.parquet')}")
