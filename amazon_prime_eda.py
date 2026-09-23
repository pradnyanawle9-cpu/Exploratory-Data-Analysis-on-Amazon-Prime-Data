import pandas as pd

# Load dataset
df = pd.read_csv("data.csv")

print("Dataset loaded successfully!")

# Basic information
print("\n--- DATASET SHAPE ---")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

# Data types
print("\n--- DATA TYPES ---")
print(df.dtypes)

# Missing values
print("\n--- MISSING VALUES ---")
print(df.isnull().sum())

# Duplicate records
print("\n--- DUPLICATE RECORDS ---")
print("Duplicates:", df.duplicated().sum())

# Content Type Analysis
print("\n--- CONTENT TYPE ---")

content_type = df["type"].value_counts()

print(content_type)

print("\nPercentage of each content type:")
print((df["type"].value_counts(normalize=True) * 100).round(2))

# Release Year Analysis
print("\n--- RELEASE YEAR ANALYSIS ---")

year_counts = df["Sum of release_year"].value_counts().sort_index()

print("\nFirst 10 years:")
print(year_counts.head(10))

print("\nLatest 10 years:")
print(year_counts.tail(10))

print("\nMost common release years:")
print(df["Sum of release_year"].value_counts().head(10))

import matplotlib.pyplot as plt

# Release Year Trend Chart
plt.figure(figsize=(12, 6))

year_counts.plot(kind="line")

plt.title("Amazon Prime Titles by Release Year")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")
plt.grid(True)

plt.tight_layout()
plt.savefig("release_year.png")
plt.show()

# Movies vs TV Shows Chart
plt.figure(figsize=(8, 6))

content_type.plot(kind="bar")

plt.title("Movies vs TV Shows on Amazon Prime")
plt.xlabel("Content Type")
plt.ylabel("Number of Titles")
plt.xticks(rotation=0)

plt.tight_layout()
plt.savefig("content_type.png")
plt.show()

# Rating Analysis
print("\n--- RATING ANALYSIS ---")

rating_counts = df["rating"].value_counts()

print("\nTop 10 Ratings:")
print(rating_counts.head(10))

# Rating Chart
plt.figure(figsize=(10, 6))

rating_counts.head(10).plot(kind="bar")

plt.title("Top 10 Content Ratings on Amazon Prime")
plt.xlabel("Rating")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("ratings.png")
plt.show()


# Genre Analysis
print("\n--- GENRE ANALYSIS ---")

genre_counts = df["listed_in"].value_counts()

print("\nTop 10 Genres:")
print(genre_counts.head(10))

# Genre Chart
plt.figure(figsize=(10, 6))

genre_counts.head(10).plot(kind="bar")

plt.title("Top 10 Genres on Amazon Prime")
plt.xlabel("Genre")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45, ha="right")

plt.tight_layout()
plt.savefig("genres.png")
plt.show()

# Duration Analysis
print("\n--- DURATION ANALYSIS ---")

print("\nSample Duration Values:")
print(df["duration"].value_counts().head(20))

# Movie Duration Analysis
print("\n--- MOVIE DURATION ANALYSIS ---")

movie_duration = df[df["type"] == "Movie"].copy()

movie_duration["duration_minutes"] = (
    movie_duration["duration"]
    .str.replace(" min", "", regex=False)
    .astype(int)
)

print("\nAverage Movie Duration:")
print(round(movie_duration["duration_minutes"].mean(), 2), "minutes")

print("\nMedian Movie Duration:")
print(movie_duration["duration_minutes"].median(), "minutes")

# Movie Duration Graph
plt.figure(figsize=(10, 6))

movie_duration["duration_minutes"].plot(
    kind="hist",
    bins=20
)

plt.title("Distribution of Movie Durations")
plt.xlabel("Duration (Minutes)")
plt.ylabel("Number of Movies")

plt.tight_layout()
plt.savefig("movie_duration.png")
plt.show()

# TV Show Seasons Analysis
print("\n--- TV SHOW SEASONS ANALYSIS ---")

tv_duration = df[df["type"] == "TV Show"].copy()

tv_duration["seasons"] = (
    tv_duration["duration"]
    .str.extract(r"(\d+)")
    .astype(int)
)

print("\nAverage TV Show Seasons:")
print(round(tv_duration["seasons"].mean(), 2))

print("\nMedian TV Show Seasons:")
print(tv_duration["seasons"].median())

print("\nMaximum TV Show Seasons:")
print(tv_duration["seasons"].max())

# TV Show Seasons Graph
plt.figure(figsize=(10, 6))

tv_duration["seasons"].value_counts().sort_index().plot(kind="bar")

plt.title("Distribution of TV Show Seasons")
plt.xlabel("Number of Seasons")
plt.ylabel("Number of TV Shows")

plt.tight_layout()
plt.savefig("tv_show_seasons.png")
plt.show()

# ============================================================
# FINAL EDA SUMMARY - KPIs + COMBINED CHARTS
# ============================================================

# KPI calculations
total_titles = len(df)
total_movies = (df["type"] == "Movie").sum()
total_tv_shows = (df["type"] == "TV Show").sum()
missing_directors = df["director"].isna().sum()

print("\n--- FINAL KPI SUMMARY ---")
print("Total Titles:", total_titles)
print("Movies:", total_movies)
print("TV Shows:", total_tv_shows)
print("Missing Director Values:", missing_directors)

# Final KPI + Content Type Summary Chart
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# -------------------------
# KPI Summary
# -------------------------
axes[0].axis("off")

axes[0].text(
    0.5, 0.85,
    "AMAZON PRIME EDA",
    ha="center",
    va="center",
    fontsize=20,
    fontweight="bold"
)

axes[0].text(
    0.5, 0.65,
    f"Total Titles\n{total_titles:,}",
    ha="center",
    va="center",
    fontsize=18
)

axes[0].text(
    0.5, 0.43,
    f"Movies\n{total_movies:,}",
    ha="center",
    va="center",
    fontsize=16
)

axes[0].text(
    0.5, 0.23,
    f"TV Shows\n{total_tv_shows:,}",
    ha="center",
    va="center",
    fontsize=16
)

# -------------------------
# Content Type Donut Chart
# -------------------------
content_values = [total_movies, total_tv_shows]
content_labels = ["Movies", "TV Shows"]

axes[1].pie(
    content_values,
    labels=content_labels,
    autopct="%1.1f%%",
    startangle=90,
    wedgeprops=dict(width=0.45)
)

axes[1].set_title("Content Type Distribution")

plt.suptitle(
    "Amazon Prime Dataset — EDA Summary",
    fontsize=20,
    fontweight="bold"
)

plt.tight_layout()

plt.savefig(
    "final_eda_summary.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()