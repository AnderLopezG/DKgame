import pyxel
import constants
import platforms
import ladders
import Mario
import barril
import random


def update():
    
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()
        
                  
    else:
        # Movement of Mario 
        
        if pyxel.btn(pyxel.KEY_RIGHT): # Move Right if his possition is correct the game will allow him. 
            
            if objMario.posy == constants.p1_y-17 or objMario.posy == constants.p2_y-17 or objMario.posy == constants.p3_y-17 or objMario.posy == constants.p4_y-17 or objMario.posy == constants.p5_y-17 or objMario.posy == constants.p6_y-17 or objMario.posy == constants.p7_y-17:
                objMario.move('right')
                objMario.MovingRight==True
                
                # Jump:
                
            global counter
            if pyxel.btnp(pyxel.KEY_SPACE):
               objMario.counter=pyxel.frame_count 
               objMario.jump('right')
           
            if (objMario.Saltando and pyxel.frame_count-objMario.counter==3):
               objMario.desjump('right')
               objMario.counter=0
               objMario.MovingRight==True
        else:
            objMario.MovingRight = False
            
        if pyxel.btn(pyxel.KEY_LEFT): # Move Left as well if his possition is correct.
            
            if objMario.posy == constants.p1_y-17 or objMario.posy == constants.p2_y-17 or objMario.posy == constants.p3_y-17 or objMario.posy == constants.p4_y-17 or objMario.posy == constants.p5_y-17 or objMario.posy == constants.p6_y-17 or  objMario.posy == constants.p7_y-17:
                objMario.move('left')
                objMario.MovingLeft==True
                
                # Jump:
                
            global counter
            if pyxel.btnp(pyxel.KEY_SPACE) :
               objMario.counter=pyxel.frame_count 
               objMario.jump('left')
               
            if (objMario.Saltando and pyxel.frame_count-objMario.counter==3):
                objMario.desjump('left')
                objMario.counter=0
                objMario.MovingLeft==True
        else:
            objMario.MovingLeft = False
        # Ladders: if Mario is in the correct possition where there is a ladder he can go up and down
        
        if pyxel.btn(pyxel.KEY_UP): # Go UP:
            # Ladder 1:
            if (objMario.posx > 170 and objMario.posx < 185):
                if (objMario.posy < 233 and objMario.posy > 195): 
                    objMario.move('up')
                    objMario.Subiendo=True
            # Ladder 2:
            if (objMario.posx > 105 and objMario.posx < 115):
                if (objMario.posy < 196 and objMario.posy > 163): 
                    objMario.move('up')
                    objMario.Subiendo=True
            # Ladder 3:
            if (objMario.posx > 175 and objMario.posx < 190):
                if (objMario.posy < 164 and objMario.posy > 129):
                    objMario.move('up')
                    objMario.Subiendo=True
            # Ladder 4:
            if (objMario.posx > 45 and objMario.posx < 55):
                if (objMario.posy < 130 and objMario.posy > 97): 
                    objMario.move('up')
                    objMario.Subiendo=True
            # Ladder 5:
            if (objMario.posx > 165 and objMario.posx < 175):
                if (objMario.posy < 98 and objMario.posy > 64):
                    objMario.move('up')                  
                    objMario.Subiendo=True
            # Ladder 6:
            if (objMario.posx > 76 and objMario.posx < 86):
                if (objMario.posy < 65 and objMario.posy > 26): 
                    objMario.move('up')
                    
            # Ladder 7:
            if (objMario.posx > 65.5 and objMario.posx < 71.5):
                if (objMario.posy < 66 and objMario.posy > 26):
                    objMario.move('up')
                    objMario.Subiendo=True
            # Ladder 8:
            if (objMario.posx > 130.5 and objMario.posx < 137.5):
                if (objMario.posy < 65 and objMario.posy > 26):
                    objMario.move('up')
                    objMario.Subiendo=True
            
                    
        if pyxel.btn(pyxel.KEY_DOWN): # Go DOWN:
            
            # Ladder 1:
            if (objMario.posx > 170 and objMario.posx < 185):
                if (objMario.posy < 231 and objMario.posy > 195): 
                    objMario.move('down')
                    objMario.Subiendo=True
            # Ladder 2:
            if (objMario.posx > 105 and objMario.posx < 115):
                if (objMario.posy < 196 and objMario.posy > 163): 
                    objMario.move('down')
                    objMario.Subiendo=True
            # Ladder 3:
            if (objMario.posx > 175 and objMario.posx < 190):
                if (objMario.posy < 164 and objMario.posy > 129):
                    objMario.move('down')
                    objMario.Subiendo=True
            # Ladder 4:
            if (objMario.posx > 45 and objMario.posx < 55):
                if (objMario.posy < 130 and objMario.posy > 97): 
                    objMario.move('down')
                    objMario.Subiendo=True
            # Ladder 5:
            if (objMario.posx > 165 and objMario.posx < 175):
                if (objMario.posy < 98 and objMario.posy > 64):
                    objMario.move('down')
                    objMario.Subiendo=True
            # Ladder 6:
            if (objMario.posx > 76 and objMario.posx < 86):
                if (objMario.posy < 64 and objMario.posy > 23): 
                    objMario.move('down')
                    objMario.Subiendo=True
            # Ladder 7:
            if (objMario.posx >65.5 and objMario.posx < 71.5):
                if (objMario.posy < 64 and objMario.posy > 26):
                    objMario.move('down')
                    objMario.Subiendo=True
            # Ladder 8:
            if (objMario.posx > 130.5 and objMario.posx < 137.5):
                if (objMario.posy < 64 and objMario.posy > 26):
                    objMario.move('down')
                    objMario.Subiendo=True
            
        # Falling from the different platforms:
        
        # Platform 1:
        if objMario.posx > 204 and (objMario.posy==constants.p2_y-17):
            for i in range (0,36):
                objMario.descend('right')
        
        # Platform 2:
        if objMario.posx < 32 and (objMario.posy==constants.p3_y-17): #42
            for i in range (0,32):
                objMario.descend('left')
        
        # Platform 3:
        if (objMario.posx > 204.0 and objMario.posy == 129): #220
            for i in range (0,34):
                objMario.descend('right')
        
        # Platform 4:
        if objMario.posx < 32 and (objMario.posy == constants.p5_y-17): #28
            for i in range (0,32):
                objMario.descend('left')
        
        # Platform 5:
        if (objMario.posx > 205) and (objMario.posy == constants.p6_y-17): #30 (P5)
            for i in range (0,33):
                objMario.descend('right')
        
        # Platform 6:        
        if objMario.posx > 194 and (objMario.posy == constants.p7_y-17): #30
            for i in range (0,39):
                objMario.descend('right')
        
        # Platform 7:        
        if objMario.posx > 242 and (objMario.posy == constants.p7_y):
            for i in range (0,36):
                objMario.descend('right')
                
        # Platform 8:
        if (objMario.posx > 140.5) and (objMario.posy == 26):
            for i in range(0,38):
                objMario.descend('right')
        
               
        
        #Until there are 10 barrels in the screen, this will be creating them  
        counter=pyxel.frame_count
        randomnum = random.randint(90,110)
        if counter % randomnum == 0:
            if len(barrels)<10:
                objBarril=barril.Barril(40,71)
                barrels.append(objBarril)
                objBarril.Newbarril = True
                counter = 0
                
        #Now, the barrels will move to the right or to the left depending on which platform they are in; and down if the platform ends.
        for barrel in barrels:
            if (barrel.posy != 238 or barrel.posx != 34):
                if barrel.posy == constants.p6_y-10 or barrel.posy == constants.p4_y-10 or barrel.posy == constants.p2_y-10: 
                    barrel.moveRight()
                    
                if barrel.posy == constants.p5_y-10 or barrel.posy == constants.p3_y-10 or barrel.posy == constants.p1_y-10: 
                    barrel.moveLeft()
                    
                if barrel.posx == 205 or barrel.posx == 32 or barrel.posx == 220 or barrel.posx == 33 or barrel.posx == 238:
                    barrel.down()  
                
               
                if (barrel.posx == 170 and barrel.posy == 71) or (barrel.posx == 50 and barrel.posy == 104) or (barrel.posx == 185 and barrel.posy ==136) or (barrel.posx == 110 and barrel.posy == 170) or (barrel.posx == 180 and barrel.posy == 202):
                    
                    if barrel.posy == (constants.p5_y-10 or constants.p3_y-10):
                        n = random.randint(0,4)
                        if n == 1 :
                            barrel.downladderP5and3()
                            
                    if barrel.posy == (constants.p4_y-10):
                        n = random.randint(0,4)
                        if n == 1 :
                            barrel.downladderP4()  
                            
                    if barrel.posy == (constants.p2_y-10):
                        n = random.randint(0,4)
                        if n == 1 :
                            barrel.downladderP2()                     
                 
        
            else:
               barrel.remove()
               barrels.remove(barrel)
               
         
            #MARIO DIES
            if objMario.posy+7==barrel.posy:
               if objMario.posx+16==barrel.posx  or objMario.posx-9==barrel.posx:
                    objMario.remove()
                    objMario.dies==True
                    objMario.lives -= 1
            
            """
            if objMario.posy==barrel.posy-6:
                if abs(barrel.posx)-abs(objMario.posx)==10:
                    objMario.remove()
 
           """
def draw():
    pyxel.cls(0) 
        
    # Horizontal Platforms:
    
    # Platform 1:
    a=0 
    for i in range(0, constants.WIDTH//8):
       pyxel.blt((objPlatform.posx)+a,objPlatform.posy, 0, 0, 0, 8, 8, colkey=0)
       a+=8
    
    # Platform 2:
    a=0  
    for i in range(0, (constants.WIDTH//8)-6):
        pyxel.blt((objPlatform2.posx)+a,objPlatform2.posy, 0, 0, 0, 8, 8, colkey=0)
        a+=8

    # Platform 3:
    a=0  
    for i in range(0, constants.WIDTH//8):
        pyxel.blt((objPlatform3.posx)+a,objPlatform3.posy, 0, 0, 0, 8, 8, colkey=0)
        a+=8
    
    # Platform 4:
    a=0  
    for i in range(0, (constants.WIDTH//8)-6):
        pyxel.blt((objPlatform4.posx) +a , objPlatform4.posy, 0, 0, 0, 8, 8, colkey=0)
        a+=8

    # Platform 5: 
    a=0   
    for i in range(0, constants.WIDTH//8):
        pyxel.blt((objPlatform5.posx) + a, objPlatform5.posy, 0, 0, 0, 8, 8, colkey=0)
        a+=8

    # Platform 6;
    a=0   
    for i in range(0, (constants.WIDTH//8)-6):
        pyxel.blt(objPlatform6.posx + a, objPlatform6.posy, 0, 0, 0, 8, 8, colkey=0)
        a+=8
   
    # Platform 7:
    a=90
    for i in range(0, (constants.WIDTH//8)-25):
        pyxel.blt(a, 42, 0, 0, 0, 8, 8, colkey=0)
        a+=8  

    # LADDERS:
    
    # Ladder 1:
    b=0
    for i in range(0,5): 
        pyxel.blt(objLadder1.posx,(objLadder1.posy)+b, 0, 0, 17,8, 6, colkey=0)
        b+=5
    
    # Ladder 2:
    b=0
    for i in range(0,5):
        pyxel.blt(objLadder2.posx,(objLadder2.posy)+b, 0, 0, 17,8, 6, colkey=0)
        b+=5
    
    # Ladder 3:
    b=0
    for i in range(0,5):
        pyxel.blt(objLadder3.posx,(objLadder3.posy)+b, 0, 0, 17,8, 6, colkey=0) 
        b+=5
    
    # Ladder 4:
    b=0
    for i in range(0,5):
        pyxel.blt(objLadder4.posx,(objLadder4.posy)+b, 0, 0, 17,8, 6, colkey=0)
        b+=5
    
    # Ladder 5:
    b=0
    for i in range(0,5):
        pyxel.blt(objLadder5.posx,(objLadder5.posy)+b, 0, 0, 17,8, 6, colkey=0) 
        b+=5
    
    # Ladder 6:
    b=0
    for i in range(0,(constants.HEIGHT//8)-25):
        pyxel.blt(objLadder6.posx,(objLadder6.posy)+b, 0, 0, 17,8, 6, colkey=0) 
        b-=5
    
    # Ladder 7:
    b=74
    for i in range(0,(constants.HEIGHT//8)-21):
        pyxel.blt(81, b, 0, 0, 17,8, 6, colkey=0) 
        b-=5
        
    # Ladder 8:
    b=74
    for i in range(0,(constants.HEIGHT//8)-21):
        pyxel.blt(70, b, 0, 0, 17,8, 6, colkey=0)
        b-=5
        
    # Static elements
    pyxel.blt(constants.oilx, constants.oily, 0, 8, 0, 16, 16, colkey=0)  #  Oil
    pyxel.blt(constants.firex, constants.firey, 0, 24, 0, 16, 16, colkey=0)  #  Fire
    pyxel.blt(0, 66, 0, 12, 103, 12, 16)  #  barril1
    pyxel.blt(13,66, 0, 12, 103, 12, 16)  #  barril2
    pyxel.blt(0, 50, 0, 12, 103, 12, 16)  #  barril3
    pyxel.blt(13, 50, 0, 12, 103, 12, 16) #  barril4
    pyxel.blt(constants.princessx, constants.princessy, 0, 6, 179, 16, 16, colkey=0)  #  princess
    pyxel.blt(25, 52, 0, 8, 213, 40, 30)  #  donkey
    pyxel.blt(constants.bonusx, constants.bonusy, 0, 181, 100,46, 20, colkey=0)  #  bonus
    pyxel.blt(constants.helpx, constants.helpy, 0, 158, 182, 23, 8, colkey=0)#help
    
    #Animating the barrels
    for barrel in barrels:
        if pyxel.frame_count%4==0:
            pyxel.blt(barrel.posx, barrel.posy,0, 35, 106, 12, 10, colkey=0)
        if pyxel.frame_count%4==1:
            pyxel.blt(barrel.posx, barrel.posy,0, 107, 106, 12, 10, colkey=0)
        if pyxel.frame_count%4==2:
            pyxel.blt(barrel.posx, barrel.posy,0, 83, 106, 12, 10, colkey=0)
        if pyxel.frame_count%4==3:
            pyxel.blt(barrel.posx, barrel.posy,0, 59, 106, 12, 10, colkey=0)
        
    # Text Lives
    pyxel.text(0,20,'LIVES',8)
    #Lives
    a=0
    
    if objMario.dies:
        for i in range(0,objMario.lives):
            pyxel.blt(a,30,0,131,8,7,8)
            a+=7
    else:
        for i in range(0,3):
            pyxel.blt(a,30,0,131,8,7,8)
            a+=7
    if objMario.posx == 117 and objMario.posy == 26:
        pyxel.blt(112,10,0,191,180,14,14)
        
    if objMario.posy==26:
     
        barrel.remove() 
        pyxel.cls(0)
        pyxel.text(120, 130, "YOU WON!!", 7)
    
    if objMario.lives==0: 
          pyxel.cls(0)
          pyxel.text(115, 130, "GAME OVER", 7)   
        
        
        
    # MARIO:
    #If Mario is running
    if objMario.Saltando==False and objMario.Subiendo==False and objMario.MovingRight==True:
      if pyxel.frame_count%2==0:
        pyxel.blt(objMario.posx,objMario.posy,0,6,32,-16,16,colkey=0) 
      if pyxel.frame_count%2==1: 
        pyxel.blt(objMario.posx,objMario.posy,0,53,33,-16,16,colkey=0) 
        
    if objMario.Saltando==False and objMario.Subiendo==False and objMario.MovingLeft==True:
      if pyxel.frame_count%2==0:
        pyxel.blt(objMario.posx,objMario.posy,0,6,32,16,16,colkey=0) 
      if pyxel.frame_count%2==1: 
        pyxel.blt(objMario.posx,objMario.posy,0,53,33,16,16,colkey=0) 
    
    #If Mario is not moving
    if objMario.MovingRight==False and objMario.MovingLeft == False:
        pyxel.blt(objMario.posx,objMario.posy,0,6,32,16,16,colkey=0) 
    
    #If Mario is jumping
    if objMario.Saltando==True:
        pyxel.blt(objMario.posx,objMario.posy,0,29,32,16,16,colkey=0)
    
    #If Mario is going up a ladder
    if objMario.Subiendo==True:
        pyxel.blt(objMario.posx,objMario.posy,0,78,32,16,16,colkey=0)
    
    
     
    
    
"""
    a=0
    i=3
    for i in range(3):
        if se muere:
            #Lives
            i-=1
            for i in range(0,i):
                pyxel.blt(a,30,0,131,8,7,8)
                a+=7
            
"""
objLadder1= ladders.Ladders(180,220)
objLadder2= ladders.Ladders(110,186)
objLadder3= ladders.Ladders(185,153)
objLadder4= ladders.Ladders(50,120)
objLadder5= ladders.Ladders(170,88)
objLadder6= ladders.Ladders(136,74)
objLadder7= ladders.Ladders(81,74)
objLadder8= ladders.Ladders(70,74)

objPlatform = platforms.Platforms (0,248)
objPlatform2 = platforms.Platforms (0,212) #36
objPlatform3 = platforms.Platforms (42,180) #32
objPlatform4 = platforms.Platforms (0,146) #34
objPlatform5 = platforms.Platforms (42,114) #32
objPlatform6 = platforms.Platforms (0,81)
objPlatform7 = platforms.Platforms (90,42)

objBarril = barril.Barril (40,71)

barrels = []
objMario = Mario.Mario (20,231)

pyxel.init(constants.WIDTH,constants.HEIGHT,caption="Donkey Kong")
pyxel.load("assets/my_resource.pyxres")
pyxel.run(update,draw)
   