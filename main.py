import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("OTT Streaming Platform Content & Catalog Insights")
print("=" * 55)

# Load dataset
df = pd.read_csv("data/NetFlix.csv")

# 2. MISSING VALUE ANALYSIS


print("\nMissing Values:")
print(df.isnull().sum())

print("\nMissing Value Percentage:")
missing_percentage = (df.isnull().sum() / len(df)) * 100
print(missing_percentage.sort_values(ascending=False))

# 3. DUPLICATE ANALYSIS

duplicate_count = df.duplicated().sum()

print("\nNumber of Duplicate Records:")
print(duplicate_count)

# 4. HANDLE MISSING VALUES

df["director"] = df["director"].fillna("Unknown")
df["cast"] = df["cast"].fillna("Unknown")
df["country"] = df["country"].fillna("Unknown")
df["rating"] = df["rating"].fillna("Unknown")

# 5. MOVIE VS TV SHOW ANALYSIS

print("\nContent Type Distribution:")
print(df["type"].value_counts())

plt.figure(figsize=(8, 5))

sns.countplot(data=df, x="type")

plt.title("Movies vs TV Shows")
plt.xlabel("Content Type")
plt.ylabel("Number of Titles")

plt.tight_layout()

plt.savefig("visualizations/movies_vs_tv_shows.png")

plt.show()

# 6. RELEASE YEAR ANALYSIS

year_counts = df["release_year"].value_counts().sort_index()

print("\nContent by Release Year:")
print(year_counts.tail(20))

plt.figure(figsize=(14, 6))

sns.lineplot(
    x=year_counts.index,
    y=year_counts.values
)

plt.title("Content Release Trend Over the Years")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")

plt.tight_layout()

plt.savefig("visualizations/release_year_trend.png")

plt.show()

# 7. GENRE ANALYSIS

genre_data = df["genres"].dropna()

genre_list = genre_data.str.split(", ").explode()

genre_counts = genre_list.value_counts()

print("\nTop 20 Genres:")
print(genre_counts.head(20))

plt.figure(figsize=(10, 7))

sns.barplot(
    x=genre_counts.head(10).values,
    y=genre_counts.head(10).index
)

plt.title("Top 10 Genres on Netflix")
plt.xlabel("Number of Titles")
plt.ylabel("Genre")

plt.tight_layout()

plt.savefig("visualizations/top_genres.png")

plt.show()

# 8. RATING ANALYSIS

rating_counts = df["rating"].value_counts()

print("\nContent Rating Distribution:")
print(rating_counts)

plt.figure(figsize=(12, 6))

sns.countplot(
    data=df,
    x="rating",
    order=df["rating"].value_counts().index
)

plt.title("Netflix Content Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Number of Titles")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("visualizations/rating_distribution.png")

plt.show()

# 9. CAST ANALYSIS

cast_data = df["cast"].dropna()

cast_list = cast_data[cast_data != "Unknown"].str.split(", ").explode()

cast_counts = cast_list.value_counts()

print("\nTop 20 Most Frequently Appearing Actors:")
print(cast_counts.head(20))

plt.figure(figsize=(10, 7))

sns.barplot(
    x=cast_counts.head(10).values,
    y=cast_counts.head(10).index
)

plt.title("Top 10 Most Frequently Appearing Actors")
plt.xlabel("Number of Titles")
plt.ylabel("Actor")

plt.tight_layout()

plt.savefig("visualizations/top_actors.png")

plt.show()

# 10. COUNTRY ANALYSIS

country_data = df["country"].dropna()

country_list = country_data[country_data != "Unknown"].str.split(", ").explode()

country_counts = country_list.value_counts()

print("\nTop 15 Content Producing Countries:")
print(country_counts.head(15))

plt.figure(figsize=(10, 7))

sns.barplot(
    x=country_counts.head(10).values,
    y=country_counts.head(10).index
)

plt.title("Top 10 Content Producing Countries")
plt.xlabel("Number of Titles")
plt.ylabel("Country")

plt.tight_layout()

plt.savefig("visualizations/top_countries.png")

plt.show()

# 11. RATING HEATMAP

rating_type = pd.crosstab(
    df["rating"],
    df["type"]
)

print("\nRating by Content Type:")
print(rating_type)

plt.figure(figsize=(10, 8))

sns.heatmap(
    rating_type,
    annot=True,
    fmt="d"
)

plt.title("Rating Distribution by Content Type")
plt.xlabel("Content Type")
plt.ylabel("Rating")

plt.tight_layout()

plt.savefig("visualizations/rating_heatmap.png")

plt.show()

# 12. DATE ANALYSIS

df["date_added"] = pd.to_datetime(
    df["date_added"],
    errors="coerce"
)

df["added_year"] = df["date_added"].dt.year

print("\nContent Added by Year:")
print(df["added_year"].value_counts().sort_index())

added_year_counts = df["added_year"].value_counts().sort_index()

plt.figure(figsize=(10, 6))

sns.lineplot(
    x=added_year_counts.index,
    y=added_year_counts.values,
    marker="o"
)

plt.title("Netflix Content Added by Year")
plt.xlabel("Year")
plt.ylabel("Number of Titles")

plt.tight_layout()

plt.savefig("visualizations/content_added_trend.png")

plt.show()

# -------------------------------
# 13. SAVE CLEANED DATASET
# -------------------------------

df.to_csv(
    "outputs/cleaned_netflix_dataset.csv",
    index=False
)

print("\nCleaned dataset saved successfully!")