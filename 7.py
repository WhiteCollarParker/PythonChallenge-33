import requests
from io import BytesIO
import re

from PIL import Image

img = Image.open(
    BytesIO(requests.get("http://www.pythonchallenge.com/pc/def/oxygen.png").content)
)
# img = Image.open(BytesIO(requests.get('http://www.pythonchallenge.com/pc/def/oxygen.png').content))

# print(f'width {img.width} : height {img.height}')

row = [img.getpixel((x, img.height / 2)) for x in range(img.width)]

row = row[::7]

list = [r for r, g, b, a in row if r == g == b]

print("".join(map(chr, list)))
vals = re.findall("\d+", "".join(map(chr, list)))

print("".join(map(chr, map(int, vals))))
print(vals)

