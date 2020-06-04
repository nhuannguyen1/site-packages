def leftstr (substr = None, symbtoplit = "_"):
    """ left side of sring """
    # len of str
    lenstr = len(substr)
    # returns first occurrence of Substring 
    result = substr.find('_',1,lenstr) 
    # return left
    return left(substr,result)


def splitstrtolist(subtr, symbtoplit = "x"):
    """split str """
    return subtr.split(symbtoplit)

def converliststrtoint(liststr = None):
    """ conver list str to int """
    res = list(map(int,liststr))
    return res

def left(s, amount):
    """ extract str left """
    return s[:amount]

def exstrtolistint (strp = None, symbtoplitp = "_",symbtoplitsecond = "x" ):
    """ return exstr of list int form string"""
    leftt = leftstr(substr=strp)
    listtr = splitstrtolist(leftt)
    return converliststrtoint (listtr)
    