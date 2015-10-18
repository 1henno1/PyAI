import json

do = ["do", "does", "did"]
have = ["have", "has", "had"]
be = ["am", "are", "is", "was", "were"]


def isIn(el, ls):
    for element in ls:
        if element == el:
            return True

def printAllObj(fileName, objArray):
    objAttrArray = []
    file = open(fileName+".json", mode="w")
    file.truncate(0)
    for obj in objArray:
        objAttrArray.append(obj.attribs())
    json.dump(objAttrArray, file)
    file.close()

def printObj(fileName, obj):
    file = open(fileName+".json", mode="w")
    json.dump(obj.attribs(), file)
    file.close()

def getObj(fileName):
    file = open(fileName+".json")
    contents = json.load(file)
    file.close()
    return(contents)
