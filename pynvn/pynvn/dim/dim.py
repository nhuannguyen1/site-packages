from pynvn.caculate.coord_point import coordp

class dim:
    """automatic dimention from top left point and bottom right point"""
    def __init__ (self, cavas = [100,100],topleftp = [0,0], 
                    bottomrightp = [100,100], 
                    arrow = "both",
                    loc_dim = "ver_center",
                    ):
        self.topleftp = topleftp
        self.bottomrightp = bottomrightp
        self.loc_dim = loc_dim
        self.arrow = arrow
        self.cavas = cavas
        # return star point and end point
        self.sepoint = coordp(topleftp=self.topleftp,bottomrightp=self.bottomrightp)
        
    def rectangle(self,*args,**kwargs):
        """ center for rectangle"""
        self.cavas .create_line( *self.sepoint,arrow=arrow)
    

    

    
    