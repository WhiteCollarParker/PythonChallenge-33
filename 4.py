from urllib.request import urlopen
import re

uri = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s"
num = 16044 / 2

while True:
    content = urlopen(uri % num).read().decode()
    print(content)
    match = re.search("and the next nothing is (\d+)", content)
    if match == None:
        break
    num = match.group(1)
    print(num)
print(match.group(1))

# How am I supposed to guess it.
# Nevertheless it's fun.
