def check_list_value (valuetocheck = ["None","nhuan"], checkvalue = [None,""]):
    """ 
    check value in list using all 
    ex1 = valuetocheck = [None,"nhuan"] heckvalue = [None,""] return False,
    ex2 = valuetocheck = ["None","nhuan"] heckvalue = [None,""] return True

    """
    return all(n not in checkvalue for n in valuetocheck)