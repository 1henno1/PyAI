from basics import *
import question, statement, string

def getInput():
    inp = input()
    inpNoPunct = inp.translate(str.maketrans('', '', string.punctuation))
    inpLower = inpNoPunct.lower()
    if isIn("?", inp):
        print(question.question(inpLower))
    if isIn(".", inp):
        statement.statement(inpLower)

while True:
    getInput()
