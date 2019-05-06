import zipfile, re

f = zipfile.ZipFile("channel.zip")
num = '90052'

comments = []
while True:
    content = f.read(num + ".txt").decode("utf-8")
    comments.append(f.getinfo(num + ".txt").comment.decode("utf-8"))
    print(content)
    match = re.search("Next nothing is (\d+)", content)
    if match == None:
        break
    num = match.group(1)

print("".join(comments))

# I wonder, if there is  really a man. Who didn't used any hints and actually 
# took his time to guess the answer. I must be frustrating to no end.