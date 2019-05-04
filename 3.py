import urllib.request
import re

html = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/equality.html").read().decode()

data = re.findall("<!--(.*?)-->", html, re.DOTALL)
data = data[-1]


output = ("".join(re.findall("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+", data)))




# Make me wanna to some regex exercises.