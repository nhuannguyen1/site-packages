from pynvn.caculate.ratio import ratio
from PIL import Image, ImageTk
import warnings
import math
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

        self.minradio = ratio(real_w=self.frameb[2],
                                    real_h=self.frameb[3],
                                    w = self.value_dis * 2,
                                    h = self.value_dis * 2).reratiomin()

        if usingcoord:
            self.cavas.bind("<MouseWheel>",self.zoomerc)
            # This is what enables using the mouse:
            self.cavas.bind("<ButtonPress-1>", self.move_start)
            self.cavas.bind("<B1-Motion>", self.move_move)
            self.sccvc()
        elif isimage:
            self.imscale = 1.0  # scale for the canvas image zoom, public for outer classes
            self.__delta = 1.3  # zoom magnitude
            self.__filter = Image.ANTIALIAS  # could be: NEAREST, BILINEAR, BICUBIC and ANTIALIAS
            self.__previous_state = 0  # previous state of the keyboard
            self.path = self.imagepath  # path to the image, should be public for outer classes
            # Bind events to the Canvas
            self.cavas.bind('<Configure>', lambda event: self.__show_image())  # canvas is resized
            self.cavas.bind('<ButtonPress-1>', self.__move_from)  # remember canvas position
            self.cavas.bind('<B1-Motion>',     self.__move_to)  # move canvas to the new position
            self.cavas.bind('<MouseWheel>', self.__wheel)  # zoom for Windows and MacOS, but not Linux
            self.cavas.bind('<Button-5>',   self.__wheel)  # zoom for Linux, wheel scroll down
            self.cavas.bind('<Button-4>',   self.__wheel)  # zoom for Linux, wheel scroll up
            # Handle keystrokes in idle mode, because program slows down on a weak computers,
            # when too many key stroke events in the same time
            self.cavas.bind('<Key>', lambda event: self.cavas.after_idle(self.__keystroke, event))
            # Decide if this image huge or not
            self.__huge = False  # huge or not
            self.__huge_size = 14000  # define size of the huge image
            self.__band_width = 1024  # width of the tile band
            Image.MAX_IMAGE_PIXELS = 1000000000  # suppress DecompressionBombError for the big image
            with warnings.catch_warnings():  # suppress DecompressionBombWarning
                warnings.simplefilter('ignore')
                self.__image = Image.open(self.path)  # open image, but down't load it
            self.imwidth, self.imheight = self.__image.size  # public for outer classes
            if self.imwidth * self.imheight > self.__huge_size * self.__huge_size and \
            self.__image.tile[0][0] == 'raw':  # only raw images could be tiled
                self.__huge = True  # image is huge
                self.__offset = self.__image.tile[0][2]  # initial tile offset
                self.__tile = [self.__image.tile[0][0],  # it have to be 'raw'
                            [0, 0, self.imwidth, 0],  # tile extent (a rectangle)
                            self.__offset,
                            self.__image.tile[0][3]]  # list of arguments to the decoder
            self.__min_side = min(self.imwidth, self.imheight)  # get the smaller image side
            # Create image pyramid
            self.__pyramid = [self.smaller()] if self.__huge else [Image.open(self.path)]
            # Set ratio coefficient for image pyramid
            self.__ratio = max(self.imwidth, self.imheight) / self.__huge_size if self.__huge else 1
            self.__curr_img = 0  # current image from the pyramid
            #self.__scale =  self.imscale * self.__ratio  # image pyramide scale
            self.__reduction = 4  # reduction degree of image pyramid
            w, h = self.__pyramid[-1].size
            while w > 512 and h > 512:  # top pyramid image is around 512 pixels in size
                w /= self.__reduction  # divide on reduction degree
                h /= self.__reduction  # divide on reduction degree
                self.__pyramid.append(self.__pyramid[-1].resize((int(w), int(h)), self.__filter))
            
            # top left and button right of rec coord
            coordrec = [self.centerp[0] - self.imwidth/2,
                        self.centerp[1] - self.imheight/2,
                        self.centerp[0] + self.imwidth/2,
                        self.centerp[1] + self.imheight/2]
            # Put image into container rectangle and use it to set proper coordinates to the image
            self.container = self.cavas.create_rectangle((coordrec), width=0,fill="blue")
            self.sccv()
            self.__scale =  self.minradio
            self.__show_image()  # show image on the canvas
            self.cavas.focus_set()  # set focus on the canvas
         
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
        """ scale in cavas """
        self.cavas.scale("all",self.centerp[0], 
                                self.centerp[1], 
                                self.minradio/1.1, 
                                self.minradio/1.1)
    
    def sccv (self):
        """ scale in cavas """
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
        self.cavas.imagetk = imagetk  # keep an extra reference to prevent garbage-collection
    
    def smaller(self):
        """ Resize image proportionally and return smaller image """
        w1, h1 = float(self.imwidth), float(self.imheight)
        w2, h2 = float(self.__huge_size), float(self.__huge_size)
        aspect_ratio1 = w1 / h1
        aspect_ratio2 = w2 / h2  # it equals to 1.0
        if aspect_ratio1 == aspect_ratio2:
            image = Image.new('RGB', (int(w2), int(h2)))
            k = h2 / h1  # compression ratio
            w = int(w2)  # band length
        elif aspect_ratio1 > aspect_ratio2:
            image = Image.new('RGB', (int(w2), int(w2 / aspect_ratio1)))
            k = h2 / w1  # compression ratio
            w = int(w2)  # band length
        else:  # aspect_ratio1 < aspect_ration2
            image = Image.new('RGB', (int(h2 * aspect_ratio1), int(h2)))
            k = h2 / h1  # compression ratio
            w = int(h2 * aspect_ratio1)  # band length
        i, j, n = 0, 1, round(0.5 + self.imheight / self.__band_width)
        while i < self.imheight:
            band = min(self.__band_width, self.imheight - i)  # width of the tile band
            self.__tile[1][3] = band  # set band width
            self.__tile[2] = self.__offset + self.imwidth * i * 3  # tile offset (3 bytes per pixel)
            self.__image.close()
            self.__image = Image.open(self.path)  # reopen / reset image
            self.__image.size = (self.imwidth, band)  # set size of the tile band
            self.__image.tile = [self.__tile]  # set tile
            cropped = self.__image.crop((0, 0, self.imwidth, band))  # crop tile band
            image.paste(cropped.resize((w, int(band * k)+1), self.__filter), (0, int(i * k)))
            i += band
            j += 1
        return image

    def redraw_figures(self):
        """ Dummy function to redraw figures in the children classes """
        pass

    def grid(self, **kw):
        """ Put CanvasImage widget on the parent widget """
        self.__imframe.grid(**kw)  # place CanvasImage widget on the grid
        self.__imframe.grid(sticky='nswe')  # make frame container sticky
        self.__imframe.rowconfigure(0, weight=1)  # make canvas expandable
        self.__imframe.columnconfigure(0, weight=1)

    def pack(self, **kw):
        """ Exception: cannot use pack with this widget """
        raise Exception('Cannot use pack with the widget ' + self.__class__.__name__)

    def place(self, **kw):
        """ Exception: cannot use place with this widget """
        raise Exception('Cannot use place with the widget ' + self.__class__.__name__)

    # noinspection PyUnusedLocal
    def __scroll_x(self, *args, **kwargs):
        """ Scroll canvas horizontally and redraw the image """
        self.cavas.xview(*args)  # scroll horizontally
        self.__show_image()  # redraw the image

    # noinspection PyUnusedLocal
    def __scroll_y(self, *args, **kwargs):
        """ Scroll canvas vertically and redraw the image """
        self.cavas.yview(*args)  # scroll vertically
        self.__show_image()  # redraw the image

    def __show_image(self):
        """ Show image on the Canvas. Implements correct image zoom almost like in Google Maps """
        box_image = self.cavas.coords(self.container)  # get image area
        #print ("box_image",box_image)
        box_canvas = (self.cavas.canvasx(0),  # get visible area of the canvas
                      self.cavas.canvasy(0),
                      self.cavas.canvasx(self.cavas.winfo_width()),
                      self.cavas.canvasy(self.cavas.winfo_height()))
        box_img_int = tuple(map(int, box_image))  # convert to integer or it will not work properly
        # Get scroll region box
        box_scroll = [min(box_img_int[0], box_canvas[0]), min(box_img_int[1], box_canvas[1]),
                      max(box_img_int[2], box_canvas[2]), max(box_img_int[3], box_canvas[3])]
        # Horizontal part of the image is in the visible area
        if  box_scroll[0] == box_canvas[0] and box_scroll[2] == box_canvas[2]:
            box_scroll[0]  = box_img_int[0]
            box_scroll[2]  = box_img_int[2]
        # Vertical part of the image is in the visible area
        if  box_scroll[1] == box_canvas[1] and box_scroll[3] == box_canvas[3]:
            box_scroll[1]  = box_img_int[1]
            box_scroll[3]  = box_img_int[3]
        # Convert scroll region to tuple and to integer
        self.cavas.configure(scrollregion=tuple(map(int, box_scroll)))  # set scroll region
        x1 = max(box_canvas[0] - box_image[0], 0)  # get coordinates (x1,y1,x2,y2) of the image tile
        y1 = max(box_canvas[1] - box_image[1], 0)
        x2 = min(box_canvas[2], box_image[2]) - box_image[0]
        y2 = min(box_canvas[3], box_image[3]) - box_image[1]
        if int(x2 - x1) > 0 and int(y2 - y1) > 0:  # show image if it in the visible area
            if self.__huge and self.__curr_img < 0:  # show huge image
                h = int((y2 - y1) / self.imscale)  # height of the tile band111
                self.__tile[1][3] = h  # set the tile band height
                self.__tile[2] = self.__offset + self.imwidth * int(y1 / self.imscale) * 3
                self.__image.close()
                self.__image = Image.open(self.path)  # reopen / reset image
                self.__image.size = (self.imwidth, h)  # set size of the tile band
                self.__image.tile = [self.__tile]
                image = self.__image.crop((int(x1 / self.imscale), 0, int(x2 / self.imscale), h))
            else:  # show normal image
                image = self.__pyramid[max(0, self.__curr_img)].crop(  # crop current img from pyramid
                                    (int(x1 / (self.__scale)), int(y1 / (self.__scale)),
                                     int(x2 / (self.__scale)), int(y2 / (self.__scale))))
            #
            imagetk = ImageTk.PhotoImage(image.resize((int(x2 - x1), 
                                                        int(y2 - y1)), self.__filter))
            imageid = self.cavas.create_image(max(box_canvas[0],
                                                box_img_int[0]),
                                               max(box_canvas[1], 
                                               box_img_int[1]),
                                               anchor='nw', 
                                               image=imagetk)
            #self.cavas.lower(imageid)  # set image into background
            self.cavas.imagetk = imagetk  # keep an extra reference to prevent garbage-collection

    def __move_from(self, event):
            """ Remember previous coordinates for scrolling with the mouse """
            self.cavas.scan_mark(event.x, event.y)

    def __move_to(self, event):
        """ Drag (move) canvas to the new position """
        self.cavas.scan_dragto(event.x, event.y, gain=1)
        self.__show_image()  # zoom tile and show it on the canvas

    def outside(self, x, y):
        """ Checks if the point (x,y) is outside the image area """
        bbox = self.cavas.coords(self.container)  # get image area
        if bbox[0] < x < bbox[2] and bbox[1] < y < bbox[3]:
            return False  # point (x,y) is inside the image area
        else:
            return True  # point (x,y) is outside the image area

    def __wheel(self, event):
        """ Zoom with mouse wheel """
        x = self.cavas.canvasx(event.x)  # get coordinates of the event on the canvas
        y = self.cavas.canvasy(event.y)
        if self.outside(x, y): return  # zoom only inside image area
        scale  = 1.0
        # Respond to Linux (event.num) or Windows (event.delta) wheel event
        if event.num == 5 or event.delta == -120:  # scroll down, smaller
            if round(self.__min_side * self.imscale) < 30: return  # image is less than 30 pixels
            self.imscale /= self.__delta
            scale        /= self.__delta
        if event.num == 4 or event.delta == 120:  # scroll up, bigger
            i = min(self.cavas.winfo_width(), self.cavas.winfo_height()) >> 1
            if i < self.imscale: return  # 1 pixel is bigger than the visible area
            self.imscale *= self.__delta
            scale        *= self.__delta
        # Take appropriate image from the pyramid
        k = self.imscale * self.__ratio * self.minradio  # temporary coefficient
        self.__curr_img = min((-1) * int(math.log(k, self.__reduction)), len(self.__pyramid) - 1)
        self.__scale = k * math.pow(self.__reduction, max(0, self.__curr_img))
        #
        self.cavas.scale('all', x, y, scale, scale)  # rescale all objects
        # Redraw some figures before showing image on the screen
        self.redraw_figures()  # method for child classes
        self.__show_image()

    def __keystroke(self, event):
        """ Scrolling with the keyboard.
            Independent from the language of the keyboard, CapsLock, <Ctrl>+<key>, etc. """
        if event.state - self.__previous_state == 4:  # means that the Control key is pressed
            pass  # do nothing if Control key is pressed
        else:
            self.__previous_state = event.state  # remember the last keystroke state
            # Up, Down, Left, Right keystrokes
            if event.keycode in [68, 39, 102]:  # scroll right, keys 'd' or 'Right'
                self.__scroll_x('scroll',  1, 'unit', event=event)
            elif event.keycode in [65, 37, 100]:  # scroll left, keys 'a' or 'Left'
                self.__scroll_x('scroll', -1, 'unit', event=event)
            elif event.keycode in [87, 38, 104]:  # scroll up, keys 'w' or 'Up'
                self.__scroll_y('scroll', -1, 'unit', event=event)
            elif event.keycode in [83, 40, 98]:  # scroll down, keys 's' or 'Down'
                self.__scroll_y('scroll',  1, 'unit', event=event)

