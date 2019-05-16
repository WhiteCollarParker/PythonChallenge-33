import re

x = "1"

for n in range(30):
    x = "".join([str(len(j) + 1)+i for i, j in re.findall(r"(\d)(\1*)", x)])
 

print(len(x))