from tkinter import messagebox

class coordp:
    """find center from 2 point"""
    def __init__ (self,topleftp = [0,0], 
                    bottomrightp = [100,100],
                    topleftk = [0,0],
                    bottomrightk = [0,0],
                    rev_point = True,
                    rev_direction = "left",
                    dis_dim = 20,
                    dis_direc = 20,
                    ):
                    self.topleftp = topleftp
                    self.bottomrightp = bottomrightp
                    self.topleftk = topleftk
                    self.bottomrightk = bottomrightk
                    self.rev_point = rev_point
                    self.dis_dim = dis_dim
                    self.rev_direction = rev_direction
                    self.dis_direc = dis_direc

    def pointstartend(self):
        """ center point"""
        if self.rev_direction == "left":

            self.spoint  = [self.topleftp[0] - self.dis_dim,
                            self.topleftp[1]]

            self.epoint  = [self.topleftp[0] - self.dis_dim,
                            self.bottomrightp[1]]

            self.centerpoint = [self.spoint[0],
                            (self.spoint[1] + self.epoint[1])/2]
        
        elif self.rev_direction == "right":
            self.spoint  = [self.bottomrightp[0]+ self.dis_dim,
                            self.bottomrightp[1]]

            self.epoint  = [self.bottomrightp[0]+ self.dis_dim,
                            self.topleftp[1]]

            self.centerpoint = [self.spoint[0],
                                self.spoint[1] + self.epoint[1]]
        
        elif self.rev_direction == "bottom": 
            self.spoint  = [self.bottomrightp[0],
                            self.bottomrightp[1] + self.dis_dim]

            self.epoint  = [self.topleftp[0],
                            self.bottomrightp[1] + self.dis_dim]

            self.centerpoint = [self.spoint[0] + self.epoint[0] ,
                                self.spoint[1]]

        elif self.rev_direction == "top": 
            self.spoint  = [self.bottomrightp[0],
                            self.topleftp[1] - self.dis_dim]

            self.epoint  = [self.topleftp[0],
                            self.topleftp[1] - self.dis_dim] 
            self.centerpoint = [(self.spoint[0] + self.epoint[0])/2,
                                self.spoint[1]]      
        else:

            messagebox.showerror(title="error message", 
                                message="Recheck rev_direction key")

        if self.rev_point:
            self.spoint_n = self.spoint 
            self.epoint_n = self.epoint 
        else:
            self.spoint_n = self.epoint 
            self.epoint_n = self.spoint 
        return [*self.spoint_n,*self.epoint_n]
    
    def centertowpoint(self):
        """ center two boy"""
        self.pointstartend()
        return  self.centerpoint
    
    def fronttowpoint(self):
        """ return front 2 point start and end """
        self.spointf = [self.bottomrightp[0] - self.dis_dim, 
                        self.topleftp[1]]
        self.epointf = [self.bottomrightp[0] - self.dis_dim,
                        self.topleftk[1]]
        return [*self.spointf,*self.epointf]

    def fronttowpointcenter(self):
        """ return front center point of start and end"""
        self.fronttowpoint()
        return [self.spointf[0],(self.spointf[1] + self.epointf[1])/2]
    
    def backtowpoint(self):
        """ return front 2 point start and end """
        self.spointb = [self.bottomrightp[0] - self.dis_dim,
                        self.bottomrightp[1]]
        self.epointb = [self.bottomrightp[0] - self.dis_dim,
                        self.bottomrightk[1]]
        return [*self.spointb,
                *self.epointb]

    def backtowpointcenter(self):
        """ return front center point of start and end"""
        self.backtowpoint()
        return [self.spointb[0],
                (self.spointb[1] + self.epointb[1])/2]

    def lefttowpoint(self):
        """ return left 2 point start and end """
        self.spointl = [self.topleftp[0],
                        self.bottomrightp[1]- self.dis_dim]
        self.epointl = [self.topleftk[0],
                        self.bottomrightp[1]- self.dis_dim]
        return [*self.spointl,
                *self.epointl]

    def lefttowpointcenter(self):
        """ return left center point of start and end"""
        self.lefttowpoint()
        return [(self.spointl[0] + self.epointl[0])/2,self.spointl[1]]

    def righttowpoint(self):
        """ return right 2 point start and end """
        self.spointr = [self.bottomrightp[0],
                        self.bottomrightp[1]- self.dis_dim]
        self.epointr = [self.bottomrightk[0],
                        self.bottomrightp[1]- self.dis_dim]
        return [*self.spointr,*self.epointr]

    def righttowpointcenter(self):
        """ return right center point of start and end"""
        self.righttowpoint()
        return [(self.spointr[0] + self.epointr[0])/2,
                self.spointr[1]]
    
    def centerpointkid(self):
        return [(self.topleftk[0] + self.bottomrightk[0])/2,
                (self.topleftk[1] + self.bottomrightk[1])/2]
    
    def frontcenterpointp(self):
        """ return front center point """
        return [(self.topleftp[0] + self.bottomrightp[0])/2,
                self.topleftp[1] - self.dis_direc]

    def backcenterpointp(self):
        """ return back center point """
        return [(self.topleftp[0] + self.bottomrightp[0])/2,
                self.bottomrightp[1] + self.dis_direc]

    def leftcenterpointp(self):
        """ return left center point """
        return [(self.topleftp[0] - self.dis_direc),(self.bottomrightp[1] + self.topleftp[1]) / 2]

    def rightcenterpointp(self):
        """ return right center point """
        return [self.bottomrightp[0] + self.dis_direc,
                (self.bottomrightp[1] + self.topleftp[1])/2]

    def centerpoinparent(self):
        return [(self.topleftp[0] + self.bottomrightp[0])/2,
                (self.topleftp[1] + self.bottomrightp[1])/2]

    @property
    def rev_direction(self):
        return self._rev_direction
    
    @rev_direction.setter
    def rev_direction(self, direction):
        self._rev_direction = direction

    @property
    def dis_dim(self):
        return self._dis_dim
    
    @dis_dim.setter
    def dis_dim(self, dis_dim):
        self._dis_dim = dis_dim





    
    




    