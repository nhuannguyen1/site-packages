
""" 
class to handing data with symbol special 
"""
class hstring:
    def  __init__(self, stringtohl = None,
                 igchar = None, 
                 path_cof = None,
                 chartorepign = None
                                        ):
        # ignore character     
        self.igchar = igchar 
        # path to conf
        self.path_cof = path_cof
        # string to handling 
        self.stringtohl = stringtohl
        #char to replace ignore character 
        self.chartorepign = chartorepign

    #string to remove char 
    def stringremoveigcharreturnspace(self):
        return self.stringtohl.translate({ord(i):self.chartorepign
                                             for i in self.igchar})

    #remove fist and end char 
    def revdupconstrfirstend(self):
        # check and replace fist string
        stfirst = self.replacecharinstrbyindex(0) if self.stringtohl[0]\
                                     in self.igchar  else self.stringtohl
        #set new parameter for stringtohl
        self.stringtohl = stfirst
        # check and replace end string
        stsecond = self.replacecharinstrbyindex(-1) if self.stringtohl[-1]\
                                     in self.igchar  else self.stringtohl
        return stsecond

    #replace char in by index from string
    def replacecharinstrbyindex (self, index):
        # convert string to list 
        tringh = list(self.stringtohl)
        #replace value index to chart replace 
        tringh[index] = self.chartorepign
        #convert to string
        st = "".join(tringh)
        return st

    # to remove continue return only single character 
    def removecontireturnsingle(self):
        tringh = list(self.stringtohl)
        i = 0 
        while i < len(tringh) - 1:
            if (tringh[i] in self.igchar and (tringh[i] == tringh[i+1])):
                del  tringh[i]
            else:
                i = i + 1
        st = "".join(tringh)
        return st