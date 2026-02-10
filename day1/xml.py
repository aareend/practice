import urllib.request
import xml.etree.ElementTree as ET

url = input("Enter location: ")
print("Retrieving", url)

data = urllib.request.urlopen(url).read()
print("Retrieved", len(data), "characters")

tree = ET.fromstring(data)

counts = tree.findall('.//count')

total = 0
for count in counts:
    total += int(count.text)

print("Count:", len(counts))
print("Sum:", total)
