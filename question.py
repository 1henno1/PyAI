from basics import *

def question(inp):
    inpArray = inp.split(" ")
    if isIn(inpArray[0], do):
        return(YN(inpArray))
    else:
        return("I'm afraid I don't know the answer to that.")

def YN(inpArray): #Assuming the format is <to do> <subject> "have" <attr value> <1-word attr>
    subj = ""
    for word in inpArray[1:]:
        if isIn(word, have):
            break
        elif word != "a" and word != "an":
            subj += word
    objects = getObj("objects")
    for obj in objects:
        if obj["name"] == subj:
            for attr in obj:
                if attr == inpArray[-1]:
                    if obj["name"][-1] != "s":
                        obj["name"] += "s"
                    return(obj["name"][0].upper() + obj["name"][1:] + " have " + obj[attr] + " " + attr + ".")
