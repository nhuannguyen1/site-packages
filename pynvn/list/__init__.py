def plus2list(list1, list2):
    """ plus 2 list and sort it """
    return sorted(list1 + list2 )

def pairiterationlist (listin):
    """ Pair iteration in list """
    return (((i), (i + 1) % len(listin))  
            for i in range(len(listin)-1))
