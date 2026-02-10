import urllib.request
import json

url = input("Enter location: ")
print("Retrieving", url)

data = urllib.request.urlopen(url).read().decode()
print("Retrieved", len(data), "characters")

info = json.loads(data)

counts = info['comments']

total = 0
for item in counts:
    total += int(item['count'])

print("Count:", len(counts))
print("Sum:", total)
