def plus2list(list1, list2):
    """ plus 2 list and sort it """
    return sorted(list1 + list2 )

def pairiterationlist (listin):
    """ Pair iteration in list """
    return (((i), (i + 1) % len(listin))  
            for i in range(len(listin)-1))

def pairlistandlist(listm, list_str):
    """ return pair of list combine list aphabe """
    #res1 =  [[list_str[0] +str(eler[0] + 1 ),list_str[1] + str(eler[1] - 1)] for eler in list(zip(listm, listm[1:])) ]
    return [str(ele[0] + ":" + ele[1]) for ele in  [[list_str[0] +str(eler[0] + 1 ),list_str[1] + str(eler[1] - 1)] for eler in list(zip(listm, listm[1:]))]]
