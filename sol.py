import pandas as pd
import os

dir1 = "test"
df1 = pd.DataFrame(columns=["phrase", "sentiment"])
for root, dirs, files in os.walk(dir1):
    for file in files:
        if file.endswith(".txt"):
            with open(os.path.join(root, file), "r") as f:
                content = f.read()
                df1 = df1._append(
                    {"phrase": content, "sentiment": os.path.basename(root)},
                    ignore_index=True,
                )
df1.to_csv("test_dataset.csv", index=False)

dir2 = "train"
df2 = pd.DataFrame(columns=["phrase", "sentiment"])
for root, dirs, files in os.walk(dir2):
    for file in files:
        if file.endswith(".txt"):
            with open(os.path.join(root, file), "r") as f:
                content = f.read()
                df2 = df2._append(
                    {"phrase": content, "sentiment": os.path.basename(root)},
                    ignore_index=True,
                )
df2.to_csv("train_dataset.csv", index=False)
