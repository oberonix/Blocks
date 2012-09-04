from PlayerCube import *
from GLRenderer import *

class BlocksGame :
    def __init__(self) :
        self.cameraX = 0
        self.cameraY = 0
        self.cameraZ = 0
        self.eyeX = 0
        self.eyeY = 0
        self.eyeZ = 0
        self.renderer = GLRenderer()

    def run(self, argv) :
        self.mapHeight = 10
        self.mapWidth = 10

        self.map = []
        for i in range(self.mapHeight) :
            self.map.append([])
            for j in range(self.mapWidth) :
                self.map[i].append([])
                if i == 5 and j == 5 :
                    self.map[i][j] = 0
                elif i == 0 or j == 0 or i == self.mapHeight - 1 or j == self.mapWidth - 1 :
                    self.map[i][j] = 2
                else :
                    self.map[i][j] = 1

        #init renderer
        self.renderer.createWindow(argv, 0, 0, 1024, 600, "Blocks", self)

        #init gamestate
        self.locX = 3
        self.cameraX = 3
        self.locY = 1
        self.cameraY = self.locY
        self.playerCube = PlayerCube(self.locX, -1 * self.locY, self.renderer)
        self.playerCube.setSpeed(5)

        #start game loop
        self.renderer.loop()

    def display(self) :
        self.renderer.clear()
        self.playerCube.render(0, 0, 0)
        self.drawMap()
        self.updateCamera()
        self.renderer.display()

    def updateCamera(self) :
        x = self.playerCube.getX() - self.cameraX
        y = self.playerCube.getY() - self.cameraY
        z = self.cameraZ
        self.cameraZ = 0
        self.cameraX = self.playerCube.getX()
        self.cameraY = self.playerCube.getY()
        self.renderer.lookAt(x, y, z, x + self.eyeX, y + self.eyeY, -6 + self.eyeZ, 0, 1, 0)

    def drawCube(self, x, y, z, r, g, b) :
        self.renderer.drawCube(r, g, b, x, y, z)

    def drawMap(self) :
        z = -7
        color = 0
        for i in range(self.mapHeight) :
            for j in range(self.mapWidth) :
                draw = self.map[i][j] == 1
                if self.map[i][j] == 2 :
                    draw = True
                    altColor = 1 if color == 0 else 0
                    self.drawCube(j, -1 * i, z + 1, altColor, altColor, altColor)
                if draw :
                    self.drawCube(j, -1 * i, z, color, color, color)
                color = 1 if color == 0 else 0
            if self.mapWidth % 2 == 0 :
                color = 1 if color == 0 else 0

    def resize(self, width, height) :
        self.renderer.resize(width, height, self.cameraX, self.cameraY - 5, -6)
        self.renderer.lookAt(0 + self.cameraX, -5 + self.cameraY, 0, self.cameraX, self.cameraY, -6, 0, 1, 0)

    def key(self, key, x, y) :
        if ord(key) == 27 :
            exit(0)
        elif key == 'q' :
            self.playerCube.setColor(0, 1, 0)
        elif key == 'w' :
            self.playerCube.setColor(1, 0, 0)
        elif key == 'e' :
            self.playerCube.setColor(0, 0, 1)
        elif key == 'r' :
            self.playerCube.setColor(1, 1, 0)
        elif key == 'u' :
            self.playerCube.setSpeed(self.playerCube.getSpeed() + 1)
        elif key == 'j' :
            self.playerCube.setSpeed(self.playerCube.getSpeed() - 1)
        elif key == 'y' :
            self.cameraZ -= .5
        elif key == 'h' :
            self.cameraZ += .5
            
        elif key == 'i' :
            self.eyeX += .5
        elif key == 'k' :
            self.eyeX -= .5
        elif key == 'o' :
            self.eyeY += .5
        elif key == 'l' :
            self.eyeY -= .5
        elif key == 'p' :
            self.eyeZ += .5
        elif key == ';' :
            self.eyeZ -= .5
        glutPostRedisplay()

    def checkMove(self, x, y) :
        #boundary check
        if x < 0 or y < 0 or y >= self.mapHeight or x >= self.mapWidth :
            return False
        if self.map[y][x] == 1 :
            return True
        return False

    def specialKeys(self, key, x, y) :
        if key == self.renderer.LEFT:
            if self.checkMove(self.locX - 1, self.locY) :
                if self.playerCube.setDirection(4) :
                    self.locX -= 1
        elif key == self.renderer.RIGHT:
            if self.checkMove(self.locX + 1, self.locY) :
                if self.playerCube.setDirection(2) :
                    self.locX += 1
        elif key == self.renderer.DOWN:
            if self.checkMove(self.locX, self.locY + 1) :
                if self.playerCube.setDirection(1) :
                    self.locY += 1
        elif key == self.renderer.UP:
            if self.checkMove(self.locX, self.locY - 1) :
                if self.playerCube.setDirection(3) :
                    self.locY -= 1