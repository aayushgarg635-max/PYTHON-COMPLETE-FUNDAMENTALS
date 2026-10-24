with open("file.txt") as f:
    content1 = f.read()

with open("poem.txt") as f:
    content2 = f.read()

if(content1==content2):
    print("yes  these files has identical content")

else:
    print("no,these files are not identical")
