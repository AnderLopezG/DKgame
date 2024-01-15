class Mario:
    counter=0
    def __init__(self, x, y):
        self.posx=x
        self.posy=y
        self.d='right'
        self.Saltando=False
        self.Subiendo=False
        self.MovingLeft= False
        self.MovingRight = False
        self.dies=False
        self.lives = 3
    """
    @property
    def posx(self):
        return self.__posx
    
    @property
    def posy(self):
        return self.__posy
    
    @property
    def d(self):
        return self.__d
    """
    #@posx.setter
    #@posy.setter
    #@d.setter
    def move(self,d):
        if d == 'left':
            self.posx -= 1
            self.MovingLeft=True
            self.Subiendo=False
        elif d == 'right':
            self.posx += 1
            self.MovingRight=True
            self.Subiendo=False
        elif d == 'up':
            self.posy -= 1
            self.Subiendo=True
            self.MovingRight=False
            self.MovingLeft=False
        elif d == 'down':
            self.posy += 1
            self.Subiendo=True
            self.MovingRight=False
            self.MovingLeft=False
            
        else:
            self.MovingRight=False
            self.MovingLeft=False
            
        
        
        
    #@posx.setter
    #@posy.setter 
    #@d.setter
    def jump(self,d):    
        if d == 'right':
            self.posx+=15
            self.posy-=15
            self.Saltando=True        
            #self.Saltando=True
        if d == 'left':
            self.posx-=15
            self.posy-=15
            #self.Saltando=True
            self.Saltando=True        

   # @posx.setter
    #@posy.setter
   # @d.setter
    def desjump(self,d): 
        if d == 'right':
            self.posx+=15
            self.posy+=15
            self.Saltando=False
        if d == 'left':
            self.posx-=15
            self.posy+=15
            self.Saltando=False
                

    #@posx.setter
   # @posy.setter 
   # @d.setter
    def descend(self,d):
        if d =='right':
            self.posx += 0.5
            self.posy += 1
            
        if d== 'left':
            self.posx -= 0.5
            self.posy += 1
            self.Saltando=False   
            
    def remove(self):
        self.posx = 20
        self.posy = 231
        self.dies = True
    