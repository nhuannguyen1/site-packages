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
        return self.subtracttowlist(self.pointcenterofparent(),
                                    [self.info_width_k/2, 
                                    self.info_height_k/2])

    def pointrightrec(self):
        """ return point rectangle on the left""" 
        return self.plustracttowlist(self.pointcenterofparent(),
                                    [self.info_width_k/2, 
                                    self.info_height_k/2])

    def pointcenterofparent (self):
        """ point center of window parent"""
        return self.plustracttowlist(self.startpoint,
                                    [self.info_width_P/2,
                                    self.info_height_p/2
                                    ]
                                    )

    def subtracttowlist(self,list1,list2):
        """sub tract 2 list"""
        difference = []
        #initialization of result list
        zip_object = zip(list1, list2)
        for list1_i, list2_i in zip_object:
            difference.append(list1_i-list2_i)
        return difference

    def plustracttowlist(self,list1,list2):
        """plus tract 2 list"""
        difference = []
        #initialization of result list
        zip_object = zip(list1, list2)

        for list1_i, list2_i in zip_object:
            difference.append(list1_i+list2_i)
        return difference



