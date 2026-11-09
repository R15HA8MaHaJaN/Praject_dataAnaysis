import pandas as pd

# Load the dataset
df = pd.read_csv("data/dataset_banglore.csv")
# Rename the column (if needed)
df = df.rename(columns={"description": "text"})
# Count duplicate text values (keeps the first occurrence)
dup_count = df["text"].duplicated().sum()
# Total rows
total = len(df)
# Percentage of duplicates
dup_pct = (dup_count / total) * 100 if total > 0 else 0
# Print results
print(f"Duplicates: {dup_count} ({dup_pct:.2f}%)")
