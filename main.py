import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("netflix_titles.csv")

df = df.drop(['cast', 'description', 'show_id', 'date_added','listed_in'], axis=1)

df = df.drop_duplicates()

duplicate_row_df = df[df.duplicated()]
print(f"Number of duplicated rows: {duplicate_row_df.shape[0]}")

df = df.dropna()

print("Missing Values After Dropping Rows:")
print(df.isnull().sum())

print("Cleaned Data:")
print(df.head(5))

print("Final Data Shape:", df.shape)

# Plot distributions (Movies vs Tv Shows)

plt.figure(figsize=(6,3))
sns.countplot(x='type',data=df)
plt.title('Distribution of Content Types')
plt.xlabel('Content type')
plt.ylabel('Count')
plt.show()

# Plot distributions of ratings

plt.figure(figsize=(8,4))
sns.countplot(x='rating',data=df, order=df['rating'].value_counts().index)
plt.title('Distribution of Rating by content')
plt.xlabel('Rating')
plt.ylabel('Count')
plt.xticks(rotation=90)
plt.show()


