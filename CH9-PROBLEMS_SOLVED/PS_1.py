f = open("poem.txt")
content = f.read()
if("twinkle" in content):
    print("the world twinkle is present in this")

else:
    print("the world twinkle isnot present in this")

f.close()
