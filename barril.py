class Barril:

    def __init__(self, x, y):
        self.__posx=x
        self.__posy=y
        #self.__Newbarril = False
    
    @property
    def posx(self):
        return self.__posx
    
    @property
    def posy(self):
        return self.__posy
    
    #@property
    #def Newbarril(self):
        #return self.__Newbarril
    
   # @Newbarril.setter
    #def Newbarril(self,v):
    #    self.__Newbarril=v
    
    def moveRight (self):
        self.__posx += 1
        
    def moveLeft (self):
        self.__posx -= 1
        
    def down (self):
        self.__posy += 1
    
    def downladderP5and3(self):
        self.__posy += 32
        
    def downladderP4(self):
        self.__posy += 34
        
    def downladderP2 (self):
        self.__posy += 36
    
    def remove(self):
        self.__posx = 40
        self.__posy = 71
        
        
 