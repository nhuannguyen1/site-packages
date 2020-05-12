class area:
    """ caculate area"""
    def __init__ (self, topleftpoint = [0,0], bottomrightpoint = [100,100]):
        self.topleftpoint = topleftpoint
        self.bottomrightpoint = bottomrightpoint
    
    def areafromtopbottompoint(self):
        """ caculation area from  top left and bottom right"""
        return (self.bottomrightpoint[1] - self.topleftpoint[1]) *  (self.bottomrightpoint[0] - self.topleftpoint[0])
