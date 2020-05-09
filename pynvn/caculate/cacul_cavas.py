from pynvn.list.twolist import towlist
class placereccenter:
    """ place center window cavas"""
    def __init__ (self,info_width_P = 100,
                    info_height_p = 100,
                    info_width_k = 100,
                    info_height_k = 100,
                    startpoint = [0,0]):


                self.startpoint = startpoint
                self.info_width_P = info_width_P
                self.info_height_p = info_height_p
                self.info_width_k = info_width_k
                self.info_height_k = info_height_k


    def pointleftrec (self):
        """ return point rectangle on the left"""
        return towlist(self.pointcenterofparent(),
                                    [self.info_width_k/2, 
                                    self.info_height_k/2
                                    ]
                                    ).subtracttowlist()

    def pointrightrec(self):
        """ return point rectangle on the left""" 
        return towlist(self.pointcenterofparent(),
                                    [self.info_width_k/2, 
                                    self.info_height_k/2
                                    ]
                                    ).plustracttowlist()

    def pointcenterofparent (self):
        """ point center of window parent"""
        return towlist(self.startpoint,
                                    [self.info_width_P/2,
                                    self.info_height_p/2
                                    ]
                                    ).plustracttowlist()


class setbackdimention:
    """set back dimention"""
    def __init__ (self,w_front = 100,
                    w_back = 100,
                    w_left = 100,
                    w_right = 100,
                    topleftpoint_p = [0,0],
                    toprightpoint_p = [100,100]):
                self.w_front = w_front
                self.w_back = w_back
                self.w_left = w_left
                self.w_right = w_right
                self.topleftpoint_p = topleftpoint_p
                self.toprightpoint_p = toprightpoint_p
    
    def topleftpoint(self):
        """ return top left of window kid"""
        return towlist (list1= self.topleftpoint_p,list2= [self.w_left,self.w_front]).plustracttowlist()

    def toprightpoint(self):
        """ return top right of window kid"""
        return towlist (list1= self.toprightpoint_p,list2= [self.w_right,self.w_back]).subtracttowlist()