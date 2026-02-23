import sys
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

if len(sys.argv) != 2:
    print("Enter Your URL: python seir_project1.py <URL>")
    sys.exit()

url = sys.argv[1]
try:
    response = requests.get(url, verify=False)
except:
    print("Cannot open URL")
    sys.exit()
soup = BeautifulSoup(response.text, "html.parser")
print(" Print page Title:")
if soup.title:
    print(soup.title.text.strip())
else:
    print("Not found")

print()
print("Print page Body text:")
print(soup.get_text())
print()
print("Print All given Links:")
for tag in soup.find_all("a"):
    link = tag.get("href")
    if link:
        print(urljoin(url, link))
