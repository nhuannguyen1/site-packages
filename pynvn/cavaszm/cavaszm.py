from pynvn.caculate.ratio import ratio
class zmcv:
    """ scale, move in cavas """
    def __init__(self, cavas,frameb,
                    value_dis = 1000, 
                    distancezx = 0,
                    distancezy = 0 ,
                    centerp =[0,0], 
                    usingcoord = False
                    ):
        self.cavas = cavas
        self.frameb = frameb
        self.value_dis = value_dis
        self.distancezx = distancezx
        self.distancezy = distancezy
        self.centerp = centerp

        if usingcoord:
            self.cavas.bind("<MouseWheel>",self.zoomerc)
            # This is what enables using the mouse:
            self.cavas.bind("<ButtonPress-1>", self.move_start)
            self.cavas.bind("<B1-Motion>", self.move_move)
            self.sccvc()
        else:

            self.cavas.bind("<MouseWheel>",self.zoomer)
            # This is what enables using the mouse:
            self.cavas.bind("<ButtonPress-1>", self.move_start)
            self.cavas.bind("<B1-Motion>", self.move_move)
            self.sccv()
    def zoomer(self,event):
        """windows zoom """
        if (event.delta > 0):
                self.cavas.scale("all",
                                    self.frameb[2]/2 - self.distancezx, 
                                    self.frameb[3]/2 - self.distancezy, 1.1, 1.1)
        elif (event.delta < 0):
                self.cavas.scale("all", 
                                    self.frameb[2]/2 - self.distancezx, 
                                    self.frameb[3]/2 - self.distancezy , 0.9, 0.9)
                self.cavas.configure(scrollregion = self.cavas.bbox("all"))
    def zoomerc(self,event):
        """windows zoom """
        if (event.delta > 0):
                self.cavas.scale("all",*self.centerp , 1.1, 1.1)
        elif (event.delta < 0):
                self.cavas.scale("all",*self.centerp , 0.9, 0.9)
                self.cavas.configure(scrollregion = self.cavas.bbox("all"))
                
    #move
    def move_start(self, event):
                self.cavas.scan_mark(event.x, event.y)
    def move_move(self, event):
                self.cavas.scan_dragto(event.x, event.y, gain=1) 
    
    def sccvc (self):
        # scale in cavas 
        self.minradio = ratio(real_w=self.frameb[2],
                                    real_h=self.frameb[3],
                                    w = self.value_dis * 2,
                                    h = self.value_dis * 2).reratiomin()

        self.cavas.scale("all",self.centerp[0], 
                                self.centerp[1], 
                                self.minradio/1.1, 
                                self.minradio/1.1)
    def sccv (self):
        # scale in cavas 
        self.minradio = ratio(real_w=self.frameb[2],
                                    real_h=self.frameb[3],
                                    w = self.value_dis * 2,
                                    h = self.value_dis * 2).reratiomin()

        self.cavas.scale("all",self.frameb[2]/2 - self.distancezx, 
                                self.frameb[3]/2- self.distancezy, 
                                self.minradio/1.1, 
                                self.minradio/1.1)