from pynvn.caculate.ratio import ratio
from PIL import Image, ImageTk
class zmcv:
    """ scale, move in cavas """
    def __init__(self, cavas,frameb,
                    value_dis = 1000, 
                    distancezx = 0,
                    distancezy = 0 ,
                    centerp =[0,0], 
                    usingcoord = False,
                    imageid = None,
                    imagepath = None,
                    isimage = False
                    ):
        self.cavas = cavas
        self.frameb = frameb
        self.value_dis = value_dis
        self.distancezx = distancezx
        self.distancezy = distancezy
        self.centerp = centerp
        #self.imscale = 1.0
        self.imageid = imageid
        self.delta = 0.9
        self.imagepath = imagepath
        if usingcoord:
            self.cavas.bind("<MouseWheel>",self.zoomerc)
            # This is what enables using the mouse:
            self.cavas.bind("<ButtonPress-1>", self.move_start)
            self.cavas.bind("<B1-Motion>", self.move_move)
            self.sccvc()
        elif isimage:
            self.text = self.cavas.create_text(centerp, anchor='center', text='Scroll to 1 zoom')

            #self.image = Image.open(self.imagepath)
            self.cavas.bind("<MouseWheel>",self.wheel)
            self.cavas.bind("<ButtonPress-1>", self.move_start)
            self.cavas.bind("<B1-Motion>", self.move_move)
            self.sccv()
            self.imscale = self.minradio 
            self.show_image()
            #self.cavas.configure(scrollregion=self.cavas.bbox('all'))
        
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

    def wheel(self, event):
        ''' Zoom with mouse wheel '''
        scale = 1

        # Respond to Linux (event.num) or Windows (event.delta) wheel event
        if event.num == 5 or event.delta == -120:
            scale        *= self.delta
            self.imscale *= self.delta
        if event.num == 4 or event.delta == 120:
            scale        /= self.delta
            self.imscale /= self.delta
        # Rescale all canvas objects
        x = self.cavas.canvasx(event.x)
        y = self.cavas.canvasy(event.y)
        self.cavas.scale('all', x,y, scale, scale)
        self.show_image()
        self.cavas.configure(scrollregion=self.cavas.bbox('all'))

    def show_image(self):
        ''' Show image on the Canvas '''
        self.image = Image.open(self.imagepath)
        if self.imageid:
            self.cavas.delete(self.imageid)
            self.imageid = None
            self.cavas.imagetk = None  # delete previous image from the canvas
        width, height = self.image.size
        new_size = int(self.imscale * width),int(self.imscale * height)
        imagetk = ImageTk.PhotoImage(self.image.resize(new_size))
        # Use self.text object to set proper coordinates
        self.imageid = self.cavas.create_image(self.cavas.coords(self.text),
                                                        anchor='center', 
                                                        image=imagetk)
        #self.cavas.lower(self.imageid)  # set it into background
        self.cavas.imagetk = imagetk  # keep an extra reference to prevent garbage-collection