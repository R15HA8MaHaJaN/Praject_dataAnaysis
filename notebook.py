import pandas as pd
df= pd.read_csv("data/dataset_banglore.csv")
#print(df.shape)
#print(df.head())
#print(df.columns)
#print(df.info())
#print(df.isnull().sum())
#print(df.duplicated().sum())
#---------------------------------------`
"""
top_10_titles = df["title"].value_counts().head(10)
for title, count in top_10_titles.items():
    print(f"count:{count}")
    print(f"title:{repr(title)}")
print("-" * 80 )
"""
#---------------------------------------

sus_check = "Very Very Bad Road and needs to be retarded urgently as badly suf..."
matching_row = df[df["title"] == sus_check]

print(matching_row)

