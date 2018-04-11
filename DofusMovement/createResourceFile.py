
with open("copyOfResources.txt",'r') as inFile, open("onlyResources.txt","w") as outFile:
    for line in inFile:
        if "Lvl" in line:
            outFile.write(line)


