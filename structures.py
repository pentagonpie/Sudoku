import pygame
import math
import random


class point:
    def __init__(self, x, y):
        if math.fabs(x) < 1e-12:
            self.x = 0
        else:
            self.x = x

        if math.fabs(y) < 1e-12:
            self.y = 0
        else:
            self.y = y


class selectable:
    def __init__(self, color, location, size, text, visible=True, interact=True):
        self.color = color
        self.location = location
        self.size = size
        self.text = text
        self.visible = visible
        self.interact = interact
        self.value = 1

    def changeColor(self, color):
        self.color = color

    def collidePoint(self, aPoint):
        if aPoint[0] > self.location.x and aPoint[0] < self.location.x + self.size.x:
            if (
                aPoint[1] > self.location.y
                and aPoint[1] < self.location.y + self.size.y
            ):
                return True
        return False

    def draw(self, screen):

        pygame.draw.rect(
            screen,
            self.color,
            [self.location.x, self.location.y, self.size.x, self.size.y],
        )
        # defining a font
        smallfont = pygame.font.SysFont("Corbel", 25)
        textColor = (245, 244, 240)
        # rendering a text written in
        # this font
        textForm = smallfont.render(self.text, True, textColor)
        # superimposing the text onto our button
        offset = 9
        if self.value != 0:
            screen.blit(
                textForm, (self.location.x + offset + 3, self.location.y + offset)
            )


class button(selectable):
    def __init__(self, color, location, size, text, visible=True, interact=True):
        selectable.__init__(self, color, location, size, text, visible, interact)

    def on(self):
        self.visible = True
        self.interact = True

    def off(self):
        self.visible = False
        self.interact = False


class textBox(selectable):
    def __init__(
        self,
        sudokuPuzzle,
        color,
        locationScreen,
        size,
        locationSquare,
        visible=True,
        interact=True,
    ):
        selectable.__init__(
            self,
            color,
            locationScreen,
            size,
            str(sudokuPuzzle.getCell(locationSquare)),
            visible,
            interact,
        )
        self.locationSquare = locationSquare
        self.selected = False
        self.sudokuPuzzle = sudokuPuzzle
        self.selfUpdate()

    # Method to get latest number from grid that this box represents, and update value to it
    def selfUpdate(self):
        self.value = self.sudokuPuzzle.getCell(self.locationSquare)
        self.text = str(self.value)

    def manualUpdate(self, val):
        self.value = val
        self.sudokuPuzzle.setCell(self.locationSquare, val)

    def setSelected(self, val):
        self.selected = val
        if val:
            self.changeColor((102, 37, 55))
        else:
            self.changeColor((207, 78, 115))

    def on(self):
        self.interact = True
        self.changeColor(self.oldColor)

    def off(self):
        self.interact = False
        self.oldColor = self.color
        self.changeColor((237, 173, 191))
