class ratio:
    "caculate ratio"
    def __init__(self,real_w,real_h,w,h):
        self.w = w
        self.h = h
        self.real_w = real_w
        self.real_h = real_h
    
    def reratiomax(self):
        """return ratio max"""
        print (self.w,self.h,self.real_w,self.real_h)
        return max([self.w/self.real_w,self.h/self.real_h])

    def reratiomin(self):
        """return ratio min"""
        return min([self.w/self.real_w,self.h/self.real_h])
    