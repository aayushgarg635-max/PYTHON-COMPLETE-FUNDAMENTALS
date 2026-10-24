with open("log.txt") as f:
    content = f.read()

if("python" in content):
    print("yes python is present")
else:
    print("no python is not in the content")
    