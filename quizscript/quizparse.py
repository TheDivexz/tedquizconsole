def parseLine(p):
    '''Returns the contents of the line as [TOKEN,VALUE]'''
    if plineEmpty(p.strip()) || pComment(p.lstrip()):
        return None
    if pRbracket(p.strip()):
        return ["}"]
    s = p.split("=",1)
    for i in s:
        i = i.strip()
    return s

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
    if p == "" || p == None:
        return True
    return False

def pStripBrackets(p):
    '''removes the \" at the start and end of strings'''
    return p.strip("\"")