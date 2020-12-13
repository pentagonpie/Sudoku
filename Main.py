import pygame
from Sudoku import sudoku
import math
import random
from structures import textBox
from structures import button
from structures import point
from datetime import datetime
import cProfile


def printTitle(screen):
    # defining a font
    smallfont = pygame.font.SysFont("comicsansms", 30)
    textColor = (5, 5, 5)
    # rendering a text written in
    # this font
    textForm = smallfont.render("SUDOKU", True, textColor)
    screen.blit(textForm, (190, 3))


def printScreen(screen, sizeX, sizeY, buttons, boxes):

    movement = int(sizeX / 13)
    screen.fill((241, 248, 242))
    offset = 120
    color = (130, 12, 255)
    boldColor = (102, 102, 153)
    weakColor = (221, 221, 238)
    startX = int(sizeX - offset)
    startY = int(sizeY - offset)

    # title
    printTitle(screen)
    # Main rectangle around entire sudoku game

    # Vertical lines
    for x in range(1, 10):
        if x == 4 or x == 7:
            thickness = 4
            color = boldColor
        else:
            thickness = 2
            color = weakColor
        pygame.draw.line(
            screen,
            color,
            (movement * x, 44),
            (movement * x, sizeY - offset - 20),
            thickness,
        )

    # Horizontal lines
    for x in range(1, 10):
        if x == 4 or x == 7:
            thickness = 5
            color = boldColor
        else:
            thickness = 2
            color = weakColor
        pygame.draw.line(
            screen,
            color,
            (44, movement * x),
            (sizeX - offset - 20, movement * x),
            thickness,
        )

    for aButton in buttons:
        if aButton.visible:
            aButton.draw(screen)

    for box in boxes:
        box.draw(screen)

    pygame.draw.rect(
        screen, boldColor, [movement, 44, sizeX - offset * 2 + 55, movement * 9 + 5], 5
    )


def update(boxes):
    for box in boxes:
        box.selfUpdate()


# if mouse is hovered on a button it
# changes to lighter shade
def hover(buttons, mouse):

    # light shade of the button
    color_light = (100, 102, 222)

    # dark shade of the button
    color_dark = (16, 19, 222)
    for aButton in buttons:
        if aButton.collidePoint(mouse) and aButton.interact:
            # print("hovering!!!")
            aButton.changeColor(color_light)
        else:
            aButton.changeColor(color_dark)


def difficultyOptionsOff():
    buttonSimple.off()
    buttonEasy.off()
    buttonMedium.off()
    buttonHard.off()
    buttonSolve.interact = True
    buttonLoad.interact = True


# gets a path to file with puzzles of sudoku in the format of one line per puzzle, and return it as a string
def getPuzzles(path):
    puzzles = []
    with open(path) as f:
        for l in f:
            line = l.rstrip()
            if line:
                puzzles.append(line)
                # print("appending @", line, "@")
    assert len(puzzles) != 0
    return puzzles


# from list of lists of puzzles by difficulty get random puzzle of difficulty, not already shown in the past (hist)
def getRandom(puzzles, difficulty, hist):
    print(len(puzzles[0]))
    rndInt = random.choice(range(len(puzzles[0])))
    nextPuzzle = puzzles[difficulty][rndInt]
    while nextPuzzle in hist:
        rndInt = random.choice(range(len(puzzles[0])))
        nextPuzzle = puzzles[difficulty][random.choice(range(rndInt))]

    return nextPuzzle


def loadClicked(boxes):
    buttonLoad.interact = False
    buttonSolve.interact = False

    for box in boxes:
        box.off()

    buttonSimple.on()
    buttonEasy.on()
    buttonMedium.on()
    buttonHard.on()


def loadPuzzle(puzzle, hist, boxes):
    global emptyPuzzle
    global solvedPuzzle
    hist.append(newPuzzle)
    print("loading puzzle: ", newPuzzle)
    difficultyOptionsOff()
    buttonLoad.on()
    mySu.setGrid(newPuzzle)
    mySu.printGrid()
    emptyPuzzle = False
    solvedPuzzle = False

    for box in boxes:
        box.on()

    update(textBoxes)


# keeps track of the selected box
currentSelected = None


def changeSelected(box):
    global currentSelected
    if currentSelected is None:
        currentSelected = box
        currentSelected.setSelected(True)
    if currentSelected == box:
        return

    currentSelected.setSelected(False)
    currentSelected = box
    currentSelected.setSelected(True)


# After user pressed key in keyboard, get the number that was pressed
def getNumber(key):
    # default number indicating no valid number was pressed
    num = -1
    if key == pygame.K_0:
        num = 0
    elif key == pygame.K_1:
        num = 1
    elif key == pygame.K_2:
        num = 2
    elif key == pygame.K_3:
        num = 3
    elif key == pygame.K_4:
        num = 4

    elif key == pygame.K_5:
        num = 5

    elif key == pygame.K_6:
        num = 6
    elif key == pygame.K_7:
        num = 7
    elif key == pygame.K_8:
        num = 8
    elif key == pygame.K_9:
        num = 9
    return num


def changeBoxNumber(puzzle, number):
    if number == -1:
        return
    global currentSelected

    if currentSelected is not None:

        old = currentSelected.value
        currentSelected.manualUpdate(number)
        valid = currentSelected.sudokuPuzzle.checkGridValid()
        if valid == 1:

            currentSelected.selfUpdate()
        else:

            currentSelected.manualUpdate(old)
            currentSelected.selfUpdate()


def main():

    mySu = sudoku()
    mySu.setGrid(
        "..........8.......2.6.9..13..19.23.7.9.51...8.6..73.5..5..6.8.9.1.........7......"
    )
    mySu.solveGrid()
    print("grid is correct: ", mySu.checkGridValid() == 2)


mySu = sudoku()


startTime = datetime.now()
# cProfile.run("main()")
main()


print("time to solve is:")
print(datetime.now() - startTime)


paths = [
    "puzzles/simple.txt",
    "puzzles/easy.txt",
    "puzzles/medium.txt",
    "puzzles/hard.txt",
]
puzzles = []
for path in paths:
    puzzles.append(getPuzzles(path))


hist = []
emptyPuzzle = True
solvedPuzzle = False


pygame.init()
sizeX = 600
sizeY = 600
screen = pygame.display.set_mode((sizeX, sizeY))

# stores the width of the
# screen into a variable
width = screen.get_width()

# stores the height of the
# screen into a variable
height = screen.get_height()

# light shade of the button
color_light = (170, 170, 170)
# dark shade of the button
color_dark = (100, 100, 100)


boxColor = (207, 78, 115)
boxColor2 = (201, 24, 74)


done = False


buttons = []
textBoxes = []

for x in range(1, 10):
    print("------")
    for y in range(1, 10):
        movement = int(sizeX / 13)
        offset = 3
        # We are enumarating through all cells in sudoku puzzle from top to bottom, left to right
        # This is not how they are stored as a data structure, compute their position using the following formulas:
        # To see how a sudoku puzzle is stored, check in Sudoku class
        location = ((x - 1) // 3, (x - 1) % 3, (y - 1) // 3, (y - 1) % 3)
        cornerPoint = point(movement * y + offset, movement * x + offset)
        print(
            "location of textbox is ",
            location,
            ", at ",
            movement * x,
            ",",
            movement * y,
        )

        textBoxes.append(textBox(mySu, boxColor, cornerPoint, point(40, 40), location))


buttonSolve = button(color_light, point(500, 40), point(80, 30), "SOLVE")
buttonLoad = button(color_light, point(500, 80), point(80, 30), "LOAD")

difficultyY = 120
offset = 32
diffSizeX = 95
diffSizeY = 30
buttonSimple = button(
    color_light,
    point(500, difficultyY),
    point(diffSizeX, diffSizeY),
    "Simple",
    False,
    False,
)
buttonEasy = button(
    color_light,
    point(500, difficultyY + offset),
    point(diffSizeX, diffSizeY),
    "Easy",
    False,
    False,
)
buttonMedium = button(
    color_light,
    point(500, difficultyY + offset * 2),
    point(diffSizeX, diffSizeY),
    "Medium",
    False,
    False,
)
buttonHard = button(
    color_light,
    point(500, difficultyY + offset * 3),
    point(diffSizeX, diffSizeY),
    "Hard",
    False,
    False,
)

buttons.append(buttonSolve)
buttons.append(buttonLoad)
buttons.append(buttonSimple)
buttons.append(buttonEasy)
buttons.append(buttonMedium)
buttons.append(buttonHard)


clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            num = getNumber(event.key)
            changeBoxNumber(mySu, num)

        # checks if a mouse is clicked
        if event.type == pygame.MOUSEBUTTONDOWN:

            # if the mouse is clicked on the
            # button the game is terminated
            if (
                buttonSolve.collidePoint(mouse)
                and buttonSolve.interact
                and not emptyPuzzle
                and not solvedPuzzle
            ):
                print("starting to solve")
                mySu.solveGrid()
                update(textBoxes)
                solvedPuzzle = True

            if buttonLoad.collidePoint(mouse) and buttonLoad.interact:
                print("clicked on load")
                loadClicked(textBoxes)

            # Chocing difficulty of puzzle to load with 4 buttons
            if buttonSimple.collidePoint(mouse) and buttonSimple.interact:
                print("pressed buttonSimple")
                newPuzzle = getRandom(puzzles, 0, hist)
                loadPuzzle(newPuzzle, hist, textBoxes)

            if buttonEasy.collidePoint(mouse) and buttonEasy.interact:
                print("pressed buttonEasy")
                newPuzzle = getRandom(puzzles, 1, hist)
                loadPuzzle(newPuzzle, hist, textBoxes)

            if buttonMedium.collidePoint(mouse) and buttonMedium.interact:
                print("pressed buttonMedium")
                newPuzzle = getRandom(puzzles, 2, hist)
                loadPuzzle(newPuzzle, hist, textBoxes)

            if buttonHard.collidePoint(mouse) and buttonHard.interact:
                print("pressed buttonHard")
                newPuzzle = getRandom(puzzles, 3, hist)
                loadPuzzle(newPuzzle, hist, textBoxes)

            for box in textBoxes:
                if box.collidePoint(mouse) and box.interact:
                    changeSelected(box)

    # stores the (x,y) coordinates into
    # the variable as a tuple
    mouse = pygame.mouse.get_pos()

    hover(buttons, mouse)

    for box in textBoxes:
        if not box.selected and box.interact:
            if box.collidePoint(mouse):
                box.changeColor(boxColor2)
            else:
                box.changeColor(boxColor)

    printScreen(screen, sizeX, sizeY, buttons, textBoxes)
    pygame.display.update()
    pygame.display.flip()
    # How many frames per second
    clock.tick(30)