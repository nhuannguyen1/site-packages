class dcavas:
    def __init__ (self, 
                    cavas = None, 
                    topp = None, 
                    bottomp = None):
        self.cavas = cavas
        self.topp = topp
        self.bottomp = bottomp
    def drec (self, **kwargs):
        """ drawing rectangle"""
        try:

            self.cavas.delete(self.rrectangle_kid ) # remove
        except:

            pass
        self.rrectangle_kid = self.cavas.create_rectangle (*self.topp,
                                                            *self.bottomp,
                                                            fill="#e79c2b")