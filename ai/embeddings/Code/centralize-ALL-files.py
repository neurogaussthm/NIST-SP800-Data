import os
import shutil

base_dir = ".."

for method_dir in os.listdir(base_dir):
    method_path = os.path.join(base_dir, method_dir)
    if not os.path.isdir(method_path) or method_dir == "Code" or "numpy" in method_dir or method_dir == "SP800":
        continue
    for filename in os.listdir(method_path):
        if filename.endswith(".parquet") and "ALL" in filename:
            path = os.path.join(method_path, filename)
            dest_path = f"../SP800/{(''.join(method_dir.split('-')[:-1])).replace('_', '')}-{filename}"
            if os.path.exists(dest_path):
                continue
            shutil.copy2(path, dest_path)
            print(f"Copied file {path} to {dest_path}")
