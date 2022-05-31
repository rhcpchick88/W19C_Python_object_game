class Player:
    def __init__(self, intitalRow, initialColumn):
        self.rowPosition = intitalRow
        self.columnPosition = initialColumn

    # TODO
    # def moveUp(self):
    def moveUp(self):
        self.rowPosition = self.rowPosition - 1
        # row -1 because the rows go from top to down, so it would be +1 if going down, therefore -1 to go back up.
    # TODO
    # def moveDown(self):
    def moveDown(self):
        self.rowPosition = self.rowPosition + 1
    # TODO
    # def moveLeft(self):
    def moveLeft(self):
        self.columnPosition = self.columnPosition -1
        # column -1 because the columns start from left to right, in order to go right it would be +1 therefore -1 for left.
    # TODO
    # def moveRight(self):
    def moveRight(self):
        self.columnPosition = self.columnPosition +1
        