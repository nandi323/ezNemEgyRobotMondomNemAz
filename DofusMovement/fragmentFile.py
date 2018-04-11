import re

with open("onlyResources.txt",'r') as inFile, open("onlyFirstResources.txt","w") as outFile:
    for line in inFile:
        alma = re.split(r'\t+', line)
        outFile.writelines(alma[0] + '\n')