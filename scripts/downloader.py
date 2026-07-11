import urllib.request
from pathlib import Path

RAW_FOLDER = Path("data/raw")

URLS = {
    "competitions":
    "https://raw.githubusercontent.com/statsbomb/open-data/master/data/competitions.json"
}


def download_file(name):

    RAW_FOLDER.mkdir(parents=True, exist_ok=True)

    url = URLS[name]

    destination = RAW_FOLDER / f"{name}.json"

    urllib.request.urlretrieve(url, destination)

    return destination