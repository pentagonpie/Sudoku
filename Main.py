import pygame
from Sudoku import sudoku
import math 

class point:

    def __init__(self,x,y):
        if math.fabs(x)<1e-12:
            self.x = 0
        else:
            self.x = x

        if math.fabs(y)<1e-12:
            self.y = 0
        else:
            self.y = y


class selectable:
    def __init__(self, color,location,size,text):
        self.color = color
        self.location = location
        self.size = size
        self.text = text

    def changeColor(self,color):
        self.color=color

    def collidePoint(self,aPoint):
        if aPoint[0] > self.location.x and aPoint[0] < self.location.x+self.size.x:
            if aPoint[1] > self.location.y and aPoint[1] < self.location.y+self.size.y:
                return True
        return False

    def draw(self,screen):

        pygame.draw.rect(screen,self.color,[self.location.x, self.location.y, self.size.x,self.size.y]) 
        # defining a font 
        smallfont = pygame.font.SysFont('Corbel',25) 
        textColor = (200,150,80)
        # rendering a text written in 
        # this font 
        textForm = smallfont.render(self.text , True , textColor) 
        # superimposing the text onto our button 
        offset = 5
        screen.blit(textForm, (self.location.x+offset+3,self.location.y+offset))


class button(selectable):
    def __init__(self, color,location,size,text):
        selectable.__init__(self,color,location,size,text)


class textBox(selectable):
    def __init__(self, color,locationScreen,size,locationSquare):
        selectable.__init__(self,color,locationScreen,size,str(mySu.getCell(locationSquare)))
        self.locationSquare = locationSquare

    def update(self):
        self.text = str(mySu.getCell(self.locationSquare))
        


def printScreen(screen,sizeX,sizeY,buttons,boxes):
    
    movement = int(sizeX/13)
    screen.fill((241,248,242))
    offset = 120
    color = (130, 12, 255)
    startX = int(sizeX-offset)
    startY = int(sizeY-offset)
    #Vertical lines
    for x in range(1,10):
        if x % 4 == 0:
            thickness = 5
            color = (102,102,153)
        else:
            thickness = 2
            color = (221,221,238)
        pygame.draw.line(screen,color,(movement*x, 0),(movement*x,sizeY-offset),thickness)

    #Horizontal lines
    for x in range(1,10):
        if y % 4 == 0:
            thickness = 5
            color = (102,102,153)
        else:
            thickness = 2
            color = (221,221,238)
        pygame.draw.line(screen,color,(0,movement*x),(sizeX-offset,movement*x),thickness)

    for aButton in buttons:
        aButton.draw(screen)

    for box in boxes:
        box.draw(screen)

def update(boxes):
    for box in boxes:
        box.update()



    # light shade of the button 
    color_light = (170,170,170) 
  
    # dark shade of the button 
    color_dark = (100,100,100) 







print("Starting program")
mySu = sudoku()

puzzle = '8.4....3..3.......5..4.6.1..1.....65.79.6...3..8....4..43..19......5........78...'
puzzle2 = '72..491.5..5........3....27.3...........1...4.4......1.62.7..1.....9.5.6.1.5.3.4.'

puzzleComplete = '743589261586412739219376458425937186967128345138645927894763512352891674671254893'



pygame.init()
sizeX = 600
sizeY = 600
screen = pygame.display.set_mode((sizeX,sizeY))

# stores the width of the 
# screen into a variable 
width = screen.get_width() 
  
# stores the height of the 
# screen into a variable 
height = screen.get_height() 

# light shade of the button 
color_light = (170,170,170) 

# dark shade of the button 
color_dark = (100,100,100) 
boxColor = (241,248,242)
boxColor2 = (183,174,242)
done = False


buttons = []
textBoxes = []
for x in range(1,10):
    for y in range(1,10):
        movement = int(sizeX/13)
        offset = 10
        location = (y//4,(y-1)%3,x//4, (x-1)%3)
        cornerPoint = point(movement*x + offset,movement*y + offset)
        textBoxes.append(textBox(boxColor, cornerPoint, point(30,30), location))


buttonSolve = button(color_light,point(500,40), point(80,30) ,"SOLVE")
buttonLoad = button(color_light,point(500,80), point(80,30) ,"LOAD")
buttons.append(buttonSolve)
buttons.append(buttonLoad)
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
        #checks if a mouse is clicked 
        if event.type == pygame.MOUSEBUTTONDOWN: 
            
        #if the mouse is clicked on the 
        # button the game is terminated 
            if buttonSolve.collidePoint(mouse): 
                mySu.solveGrid()
                update(textBoxes)

            if buttonLoad.collidePoint(mouse): 
                mySu.setGrid(puzzle)
                update(textBoxes)

        #  pressed = pygame.key.get_pressed()
        # if pressed[pygame.K_UP]: changeViewAngle(1)
        # if pressed[pygame.K_DOWN]: changeViewAngle(0)
        

    #aCube.update()

    # stores the (x,y) coordinates into 
    # the variable as a tuple 
    mouse = pygame.mouse.get_pos()

    # if mouse is hovered on a button it 
    # changes to lighter shade  
    if buttonSolve.collidePoint(mouse): 
        buttonSolve.changeColor(color_light)
          
    else: 
        buttonSolve.changeColor(color_dark)


    
    # if mouse is hovered on a button it 
    # changes to lighter shade  
    if buttonLoad.collidePoint(mouse): 
        buttonLoad.changeColor(color_light)
          
    else: 
        buttonLoad.changeColor(color_dark)
      
    for box in textBoxes:
        if box.collidePoint(mouse):
            box.changeColor(boxColor2)
        else:
            box.changeColor(boxColor)

    printScreen(screen,sizeX,sizeY,buttons,textBoxes)          
    pygame.display.update()
    pygame.display.flip()
    #How many frames per second
    clock.tick(10)


