import pygame
import os
from TicTacToe import Button, Block

pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'  # this centers the window to the center of the user's screen

# Color definitions
white = (255, 255, 255)
black = (0, 0, 0)
buttonRed = (249, 52, 52)
hoverButtonRed = (249, 97, 97)
blue = (0, 0, 255)
buttonBlue = (108, 162, 247)
hoverButtonBlue = (138, 180, 247)

# Importing font
titleFont = pygame.font.SysFont("cambria", 30)
buttonFont = pygame.font.SysFont("cambria", 20)
blockFont = pygame.font.Font("ARLRDBD.ttf", 50)

displayWidth = 505
displayHeight = 505
centerDisplayWidth = displayWidth / 2
centerDisplayHeight = displayHeight / 2
buttonHeight = 50
buttonWidth = 180
borderWidth = 20
boxSize = 70
halfBoxSize = boxSize / 2

gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("Tic Tac Toe")
pygame.display.set_icon(pygame.image.load('icon.png'))

singlePlayer = Button.button(buttonBlue, hoverButtonBlue, gameDisplay, "SINGLE PLAYER",
                             centerDisplayWidth - (buttonWidth / 2),
                             centerDisplayHeight - 70, buttonWidth, buttonHeight, white, -70, centerDisplayWidth,
                             centerDisplayHeight, buttonFont)

twoPlayer = Button.button(buttonBlue, hoverButtonBlue, gameDisplay, "TWO PLAYER",
                          centerDisplayWidth - (buttonWidth / 2),
                          centerDisplayHeight, buttonWidth, buttonHeight, white, 0, centerDisplayWidth,
                          centerDisplayHeight, buttonFont)

quitButton = Button.button(buttonRed, hoverButtonRed, gameDisplay, "QUIT",
                           centerDisplayWidth - (buttonWidth / 2),
                           centerDisplayHeight + 70, buttonWidth, buttonHeight, white, 70, centerDisplayWidth,
                           centerDisplayHeight, buttonFont)

block0 = Block.block(gameDisplay, centerDisplayWidth - halfBoxSize - 5 - boxSize, 100, boxSize, boxSize, white,
                     blockFont)
block1 = Block.block(gameDisplay, centerDisplayWidth - halfBoxSize + 5, 100, boxSize, boxSize, white, blockFont)
block2 = Block.block(gameDisplay, centerDisplayWidth - halfBoxSize + 15 + boxSize, 100, boxSize, boxSize, white,
                     blockFont)
block3 = Block.block(gameDisplay, centerDisplayWidth - halfBoxSize - 5 - boxSize, 100 + boxSize + 10, boxSize,
                     boxSize, white, blockFont)
block4 = Block.block(gameDisplay, centerDisplayWidth - halfBoxSize + 5, 100 + boxSize + 10, boxSize, boxSize,
                     white, blockFont)
block5 = Block.block(gameDisplay, centerDisplayWidth - halfBoxSize + 15 + boxSize, 100 + boxSize + 10, boxSize,
                     boxSize, white, blockFont)
block6 = Block.block(gameDisplay, centerDisplayWidth - halfBoxSize - 5 - boxSize, 100 + (boxSize + 10) * 2, boxSize,
                     boxSize, white, blockFont)
block7 = Block.block(gameDisplay, centerDisplayWidth - halfBoxSize + 5, 100 + (boxSize + 10) * 2, boxSize, boxSize,
                     white, blockFont)
block8 = Block.block(gameDisplay, centerDisplayWidth - halfBoxSize + 15 + boxSize, 100 + (boxSize + 10) * 2,
                     boxSize, boxSize, white, blockFont)

blockFlags = [""] * 9
moves = ["X", "O"]
moveFlag = False
currentPlayer = 0
onStartScreen = True


def startScreen():
    global onStartScreen
    while True:
        configureBackground()
        handleEvents()

        singlePlayer.showButton()
        twoPlayer.showButton()
        quitButton.showButton()

        if singlePlayer.isHovered(getCursorPos()) and isLeftMouseClicked():
            singlePlayerMode()
        elif twoPlayer.isHovered(getCursorPos()) and isLeftMouseClicked():
            twoPlayerMode()
        elif quitButton.isHovered(getCursorPos()) and isLeftMouseClicked():
            quit()

        put_message_center("Tic Tac Toe", black, titleFont, 150)
        pygame.display.update()


def singlePlayerMode():
    while True:
        handleEvents()
        configureBackground()
        crossStyle()
        pygame.display.update()


def twoPlayerMode():
    global blockFlags
    global moveFlag
    global onStartScreen

    while True:
        handleEvents()
        configureBackground()
        crossStyle()
        displayCurrentPlayer(checkWin())

        if not onStartScreen and not checkWin():
            if block0.wasClicked(getCursorPos(), isLeftMouseClicked()) or blockFlags[0] != "":
                if blockFlags[0] == "":
                    blockFlags[0] = getMove(True)
                block0.putMove(blockFlags[0], buttonRed)

            if block1.wasClicked(getCursorPos(), isLeftMouseClicked()) or blockFlags[1] != "":
                if blockFlags[1] == "":
                    blockFlags[1] = getMove(True)
                block1.putMove(blockFlags[1], buttonRed)

            if block2.wasClicked(getCursorPos(), isLeftMouseClicked()) or blockFlags[2] != "":
                if blockFlags[2] == "":
                    blockFlags[2] =\
                        getMove(True)
                block2.putMove(blockFlags[2], buttonRed)

            if block3.wasClicked(getCursorPos(), isLeftMouseClicked()) or blockFlags[3] != "":
                if blockFlags[3] == "":
                    blockFlags[3] = getMove(True)
                block3.putMove(blockFlags[3], buttonRed)

            if block4.wasClicked(getCursorPos(), isLeftMouseClicked()) or blockFlags[4] != "":
                if blockFlags[4] == "":
                    blockFlags[4] = getMove(True)
                block4.putMove(blockFlags[4], buttonRed)

            if block5.wasClicked(getCursorPos(), isLeftMouseClicked()) or blockFlags[5] != "":
                if blockFlags[5] == "":
                    blockFlags[5] = getMove(True)
                block5.putMove(blockFlags[5], buttonRed)

            if block6.wasClicked(getCursorPos(), isLeftMouseClicked()) or blockFlags[6] != "":
                if blockFlags[6] == "":
                    blockFlags[6] = getMove(True)
                block6.putMove(blockFlags[6], buttonRed)

            if block7.wasClicked(getCursorPos(), isLeftMouseClicked()) or blockFlags[7] != "":
                if blockFlags[7] == "":
                    blockFlags[7] = getMove(True)
                block7.putMove(blockFlags[7], buttonRed)

            if block8.wasClicked(getCursorPos(), isLeftMouseClicked()) or blockFlags[8] != "":
                if blockFlags[8] == "":
                    blockFlags[8] = getMove(True)
                block8.putMove(blockFlags[8], buttonRed)

            if moveFlag:
                moveFlag = False
                playerFlag()

            pygame.display.update()
        else:
            if not isLeftMouseClicked():
                onStartScreen = False


def crossStyle():
    gameDisplay.fill(black, [centerDisplayWidth - halfBoxSize - 5, 100, 10, 230])
    gameDisplay.fill(black, [centerDisplayWidth + halfBoxSize + 5, 100, 10, 230])
    gameDisplay.fill(black, [centerDisplayWidth - boxSize - halfBoxSize - 5, 100 + boxSize, 230, 10])
    gameDisplay.fill(black, [centerDisplayWidth - boxSize - halfBoxSize - 5, 100 + (boxSize * 2) + 10, 230, 10])

    block0.showBlock()
    block1.showBlock()
    block2.showBlock()
    block3.showBlock()
    block4.showBlock()
    block5.showBlock()
    block6.showBlock()
    block7.showBlock()
    block8.showBlock()


def configureBackground():
    gameDisplay.fill(buttonBlue)
    gameDisplay.fill(white, [borderWidth, borderWidth, displayWidth - (borderWidth * 2),
                             displayHeight - (borderWidth * 2)])


def put_message_center(message, color, font, yOffset):
    screen_text = font.render(message, True, color)
    gameDisplay.blit(screen_text, [centerDisplayWidth - (screen_text.get_rect().width / 2), centerDisplayHeight -
                                   yOffset])


def displayCurrentPlayer(win):
    if not win:
        put_message_center("Current Player: " + getMove(False), black, titleFont, 200)
    else:
        put_message_center("Player " + moves[0 if currentPlayer == 1 else 1] + " wins!", black, titleFont, 200)


def getMove(flag):
    global moveFlag
    moveFlag = flag

    return moves[currentPlayer]


def playerFlag():
    global currentPlayer

    currentPlayer = 0 if currentPlayer == 1 else 1


def getCursorPos():
    return pygame.mouse.get_pos()


def isLeftMouseClicked():
    return pygame.mouse.get_pressed()[0]


def handleEvents():
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            quitProgram()


def checkWin():
    winPositions = [[0, 1, 2],
                    [3, 4, 5],
                    [6, 7, 8],
                    [0, 3, 6],
                    [1, 4, 7],
                    [2, 5, 8],
                    [0, 4, 8],
                    [2, 4, 6]]

    for i in range(winPositions.__len__()):
        pos = [blockFlags[winPositions[i][0]], blockFlags[winPositions[i][1]], blockFlags[winPositions[i][2]]]
        if pos[0] != "" and pos[1] != "" and pos[2] != "" and pos[0] == pos[1] and pos[1] == pos[2]:
            playerFlag()
            return True

    return False


def quitProgram():
    """
    This function quits the program.
    :return:
    """
    pygame.quit()
    exit()


while True:
    startScreen()
