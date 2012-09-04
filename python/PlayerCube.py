from math import sin, cos, pi

class PlayerCube :
    def __init__(self, x, y, renderer) :
        self.angle = 0
        self.sideDir = 1
        self.forwardDir = 0
        self.startTime = 0
        self.actionRunning = False
        self.posX = x
        self.posY = y
        self.baseZ = -6
        self.posZ = -6
        self.totalAdded = 0
        self.r = 0
        self.g = 1
        self.b = 0
        self.speed = 1
        self.direction = 0
        self.radianFactor = pi / 180
        self.renderer = renderer
        self.actionTime = 0

    def getX(self) :
        return self.posX

    def getY(self) :
        return self.posY
        
    def setColor(self, rVal, gVal, bVal) :
        self.r = rVal
        self.g = gVal
        self.b = bVal

    def setSpeed(self, newSpeed) :
        self.speed = newSpeed
        
    def getSpeed(self) :
        return self.speed

    def setDirection(self, direction) :
        if not self.actionRunning :
            self.angle = 0
            self.startTime = self.renderer.getElapsedTime()
            self.actionRunning = True
            self.forwardDir = 0
            self.sideDir = 0
            if direction == 1 :
                self.forwardDir = 1
            elif direction == 2 :
                self.sideDir = 1
            elif direction == 3 :
                self.forwardDir = -1
            elif direction == 4 :
                self.sideDir = -1
            return True
        return False
        
    def render(self, cameraX, cameraY, cameraZ) :
        self.actionTime = self.speed * (self.renderer.getElapsedTime() - self.startTime) / 1000.0
        a = 0
        if self.actionRunning :
            if self.actionTime > 1 :
                self.actionRunning = False
                self.actionTime = 0
                a = 90
                if not self.sideDir == 0 :
                    self.posX += self.sideDir * (1 - self.totalAdded)
                if self.forwardDir != 0 :
                    self.posY += -1 * self.forwardDir * (1 - self.totalAdded)
                self.totalAdded = 0
                self.posZ = self.baseZ
            else :
                a = self.actionTime * 90.0
                vOffset = .71 * sin(self.radianFactor * (a + 45))
                if self.actionTime > 0.5 :
                    vOffset = .71 * cos(self.radianFactor * (a - 45))
                vOffset -= .5

                self.posZ = vOffset + self.baseZ
                if self.sideDir != 0 :
                    self.posX += self.sideDir * (self.actionTime - self.totalAdded)
                    self.totalAdded = self.actionTime
                if self.forwardDir != 0 :
                    self.posY += -1 * self.forwardDir * (self.actionTime - self.totalAdded)
                    self.totalAdded = self.actionTime

        self.renderer.drawCube(self.r, self.g, self.b, self.posX + cameraX, self.posY + cameraY, self.posZ + cameraZ, a, self.forwardDir, self.sideDir, 0)