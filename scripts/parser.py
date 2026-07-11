import json


def load_json(file_path):

    with open(file_path, encoding="utf-8") as f:
        return json.load(f)


def competitions(data):

    result = {}

    for item in data:

        key = (
            item["competition_id"],
            item["season_id"]
        )

        result[key] = {

            "competition_id": item["competition_id"],
            "season_id": item["season_id"],

            "country": item["country_name"],
            "league": item["competition_name"],

            "season": item["season_name"]
        }

    return sorted(
        result.values(),
        key=lambda x: (
            x["country"],
            x["league"],
            x["season"]
        )
    )