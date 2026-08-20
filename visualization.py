import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/imdbCleaned.csv")

print(df.head())
print(df.info())
plt.hist(df["Rate"], bins=10)

plt.xlabel("IMDb Rating")
plt.ylabel("Number of Movies")
plt.title("Distribution of IMDb Ratings")

plt.show()
plt.scatter(df["Votes"], df["Rate"])

plt.xticks(
    range(0, 3_500_000, 500_000),
    ["0", "500K", "1M", "1.5M", "2M", "2.5M", "3M"]
)

plt.xlabel("Number of Votes")
plt.ylabel("IMDb Rating")
plt.title("IMDb Rating vs Number of Votes")

plt.show()
bins = range(1930, 2031, 10)

plt.hist(df["Year"], bins=bins)

plt.xlabel("Release Year")
plt.ylabel("Number of Movies")
plt.title("IMDb Top 250 Movies by Decade")

plt.show()
bins = range(60, 301, 20)

plt.hist(df["Runtime"], bins=bins)

plt.xlabel("Runtime (Minutes)")
plt.ylabel("Number of Movies")
plt.title("Distribution of Movie Runtime")

plt.show()
