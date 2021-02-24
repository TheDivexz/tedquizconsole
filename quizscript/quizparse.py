import re

def pComment(p):
    '''Checks if the line is a comment'''
    if p[0] == "#":
        return True
    return False

def pRbracket(p):
    '''checks if the line is a closing bracket'''
    if p == "}":
        return True
    return False

def plineEmpty(p):
    '''checks to see if line is empty'''
    if(p == "" or p == None):
        return True
    return False

def pStripBrackets(p):
    '''removes the \" at the start and end of strings'''
    return p.strip("\"")

def pList(p):
    '''parses a list in .txt files for incorrect and category setters'''
    temp = re.split('" *, *"',p)
    for t in temp:
        t.strip("\"")
    return temp


def parseLine(p):
    '''Returns the contents of the line as [TOKEN,VALUE]'''
    str1 = ""
    for el in p:
        str1 += el
    s = str1.split("=",1)
    sl = [item.strip() for item in s]
    return sl