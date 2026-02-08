
#! Word Search

with open("/Applications/Career/Python/File/practiceQ.txt", "r") as f:
    data = f.read()
    if "search" in data:
        print("Word found")
    else:
        print("Not found")
