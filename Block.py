class block(object):
    def __init__(self, display, left, top, width, height, colour, font):
        self.display = display
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.font = font
        self.colour = colour
        self.centered = width / 2

    def showBlock(self):
        self.display.fill(self.colour, [self.left, self.top, self.width, self.height])

    def putMove(self, move, textColour):
        displayText = self.font.render(move, True, textColour)
        self.display.blit(displayText, [self.left + self.centered - (displayText.get_rect().width / 2),
                                        self.top + self.centered - (displayText.get_rect().height / 2)])

    def wasClicked(self, hover, click):
        return (self.left < hover[0] < self.left + self.width) and (self.top < hover[1] < self.top + self.height) and \
               click

    def showWinningColour(self, newColour):
        self.display.fill(newColour, [self.left, self.top, self.width, self.height])

