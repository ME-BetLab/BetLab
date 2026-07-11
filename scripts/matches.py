from pathlib import Path
import urllib.request

RAW_FOLDER = Path("data/raw")

BASE_URL = "https://raw.githubusercontent.com/statsbomb/open-data/master/data/matches"


def download_matches(competition_id, season_id):

    RAW_FOLDER.mkdir(parents=True, exist_ok=True)

    filename = f"matches_{competition_id}_{season_id}.json"

    destination = RAW_FOLDER / filename

    url = f"{BASE_URL}/{competition_id}/{season_id}.json"

    urllib.request.urlretrieve(url, destination)

    return destination