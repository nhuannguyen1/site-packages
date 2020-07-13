def plus2list(list1, list2):
    """ plus 2 list and sort it """
    return sorted(list1 + list2 )

def pairiterationlist (listin):
    """ Pair iteration in list 
    ex1: [0, 1, 2, 3, 4, 5] --> [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
    ex2: ["a", "f","n", 3, 4, 5] --> [('a', 'f'), ('f', 'n'), ('n', 3), (3, 4), (4, 5)]
    """
    return list(zip(listin, listin[1:]))

def pairlistandlist(listm, list_str):
    """ return pair of list combine list aphabe """
    #res1 =  [[list_str[0] +str(eler[0] + 1 ),list_str[1] + str(eler[1] - 1)] for eler in list(zip(listm, listm[1:])) ]
    return [str(ele[0] + ":" + ele[1]) for ele in  [[list_str[0] +str(eler[0] + 1 ),list_str[1] + str(eler[1] - 1)] for eler in list(zip(listm, listm[1:]))]]
