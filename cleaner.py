import pandas as pd

df = pd.read_csv("data/imdb_raw.csv")
df["Year"] = pd.to_numeric(df["Year"], errors="coerce")
df["Rate"]= pd.to_numeric(df["Rate"], errors="coerce")
def convert_time(runTime):
    hours = 0
    minutes = 0
    if "h" in runTime:
        hours = int(runTime.split("h")[0].strip())
    if "m" in runTime:
        minutesPart = runTime.split("h")[-1]
        minutes = int(minutesPart.replace("m", "").strip())
    return hours*60 + minutes
df["Runtime"] = df["Runtime"].apply(convert_time)
def convert_votes(votes):
    votes = votes.replace("(", "").replace(")", "")
    if "M" in votes:
        return float(votes.replace("M", "")) * 1_000_000

    elif "K" in votes:
        return float(votes.replace("K", "")) * 1_000

    else:
        return float(votes)
df["Votes"] = df["Votes"].apply(convert_votes)
print(df.isnull().sum())
print("Duplicates:", df.duplicated().sum())
df.to_csv("data/imdbCleaned.csv", index=False)
