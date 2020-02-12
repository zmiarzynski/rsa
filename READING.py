
theInts = []
with open("nowytekst.txt","r") as theFile:
    for val in theFile.read().split():
        theInts.append(int(val))
    theFile.close()

print(theInts)