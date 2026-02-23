import sys
import requests
from bs4 import BeautifulSoup
import re
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

if len(sys.argv) != 3:
    print("Enter your Urls: python seir_project2.py <URL1> <URL2>")
    sys.exit()

url_name1 = sys.argv[1]
url_name2 = sys.argv[2]

def find_word(url_name):
    try:
        x1 = requests.get(url_name, verify=False)
        soup = BeautifulSoup(x1.text, "html.parser")

        for y in soup(["script", "style"]):
            y.extract()

        return soup.get_text()

    except:
        print("Cannot open URL")
        sys.exit()

def word_hash_conv(word):
    val = 0
    for c in word:
        val = (val * 31 + ord(c)) % (2**64)
    return val

def cal_simhash(text):
    bits = [0] * 64
    words = re.findall(r"[a-zA-Z0-9]+", text.lower())

    for word in words:
        h = word_hash_conv(word)

        for i in range(64):
            if h & (1 << i):
                bits[i] += 1
            else:
                bits[i] -= 1

    result = 0
    for i in range(64):
        if bits[i] > 0:
            result += (1 << i)

    return result

def find_similar(h1, h2):
    equal_bits = 0

    for i in range(64):
        b1 = (h1 >> i) & 1
        b2 = (h2 >> i) & 1

        if b1 == b2:
            equal_bits += 1

    return (equal_bits / 64) * 100

def find_common_bits(h1, h2):
    count=0
    for i in range(64):
        b1 = (h1 >> i) & 1
        b2 = (h2 >> i) & 1

        if b1 == b2:
            count += 1

    return count

text1 = find_word(url_name1)
text2 = find_word(url_name2)
h1 = cal_simhash(text1)
h2 = cal_simhash(text2)
print("No of common bits ", find_common_bits(h1, h2))
print("Similarity:", find_similar(h1, h2), "%")
