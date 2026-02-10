import urllib.request
from bs4 import BeautifulSoup

url = input("Enter - ")

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('span')

count = 0
total = 0

for tag in tags:
    num = int(tag.text)
    total += num
    count += 1

print("Count", count)
print("Sum", total)
