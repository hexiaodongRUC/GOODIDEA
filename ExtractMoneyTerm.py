#coding: utf-8

def getTargetTerm(oneline, resultFile):
    oneterm = oneline.split("\n")[0].split("\t")[0]
    if oneterm.endswith("费") or oneterm.endswith("金") or oneterm.endswith("款"):
        print oneterm
        resultFile.write(oneterm+"\n")

def processFile():
    fp = file("/Users/feiran/Documents/program/python/GOODIDEA/law-item-name", "r")
    resultFile = file("/Users/feiran/Documents/program/python/GOODIDEA/money-item-name", "a")
    while True:
        oneline = fp.readline()
        if not oneline:
            break
        getTargetTerm(oneline, resultFile)
    fp.close()
    resultFile.close()

if __name__ == '__main__':
    processFile()