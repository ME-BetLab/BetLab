from scripts.downloader import download_file
from scripts.parser import load_json, competitions

print("Downloading...")

file = download_file("competitions")

print("Parsing...")

data = load_json(file)

leagues = competitions(data)


print()

print(f"League Count : {len(leagues)}")

for league in leagues:

    print(
        league["country"],
        "-",
        league["league"]
    )
from scripts.matches import download_matches

print("\nSearching Premier League...")

premier = None

for league in leagues:

    if (
        league["country"] == "England"
        and
        league["league"] == "Premier League"
    ):
        premier = league
        break

print(
    f"Downloading {premier['league']} - {premier['season']}"
)

file = download_matches(
    premier["competition_id"],
    premier["season_id"]
)

print("Saved to:")
print(file)