#Roger Robinson

mFile = input("Name of file")
tFile = open(file, "t")
sFile = open("aye.txt", "s")
count = 0

for sentence in tFile:
    count = count + 1
    List = str(count) + " " + sentence
    mFile.close()
    sFile()
