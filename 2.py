import urllib.request
import re

html = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/ocr.html").read().decode()

data = re.findall("<!--(.*?)-->", html, re.DOTALL)
data = data[-1]


count = {}

for char in data:
    count[char] = count.get(char, 0) +  1

print(count)

key = " "
for k, v in count.items():
    if v == 1:
        key += k
print(key)

# Every time I look at hints or "right" solutions. I have a deep feeling of 
# inferiority, but I know it's going to dissapear.