from basics import *
import string

objects = []

class Obj(object):
    def __init__(self, name, attr, attrValue):
        self.name = name
        self.__dict__.update({attr: attrValue})

    def attribs(self):
        return(self.__dict__)

    
def statement(inp):
    inpArray = inp.split(" ")
    for el in inpArray:
        if isIn(el, be):
            toBe(inpArray)
        elif isIn(el, have):
            toHave(inpArray)

def toBe(inpArray):
    pass

def toHave(inpArray): #Assuming that the input is formed: <object name> <to have> <description of property - 1 or more words> <property - 1 word>, e.g. "An octopus has 8 legs."
    name = findName(inpArray)
    attr = findAttr(inpArray)
    attrValue = findAValue(inpArray)
            
    objects.append(Obj(name, attr, attrValue))
    printAllObj("objects", objects)

def findName(inpArray):
    name = ""
    if inpArray[0] == "a" or inpArray[0] == "an" or inpArray[0] == "the":
        for word in inpArray[1:]:
            if not isIn(word, have):
                name += word
                name += " "
            else:
                break
    else:
        for word in inpArray:
            if not isIn(word, have):
                name += word
                name += " "
            else:
                break
    return name[:-1]

def findAttr(inpArray):
    return inpArray[-1]

def findAValue(inpArray):
    haveFound = False
    AttrValue = ""
    for word in inpArray[:-1]:
        if haveFound == True:
            AttrValue += word
            AttrValue += " "
        elif isIn(word, have):
            haveFound = True
    return AttrValue[:-1]
