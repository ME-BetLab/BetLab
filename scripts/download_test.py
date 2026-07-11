import urllib.request

url = "https://raw.githubusercontent.com/statsbomb/open-data/master/data/competitions.json"

print("Connecting...")

try:
    response = urllib.request.urlopen(url)
    print("SUCCESS")
    print("Status:", response.status)
    print("Downloaded:", len(response.read()), "bytes")
except Exception as e:
    print("ERROR")
    print(e)