#include "PlayerCube.h"

PlayerCube::PlayerCube(double x, double y) {
    angle = 0;
    sideDir = 1;
    forwardDir = 0;
    startTime = 0;
    actionRunning = false;
    posX = x;
    posY = y;
    baseZ = -6;
    posZ = -6;
    totalAdded = 0;
    r = 0;
    g = 1;
    b = 0;
}

double PlayerCube::getX() {
    return posX;
}

double PlayerCube::getY() {
    return posY;
}

void PlayerCube::setColor(double rVal, double gVal, double bVal) {
    r = rVal;
    g = gVal;
    b = bVal;
}

void PlayerCube::setSpeed(double newSpeed) {
    speed = newSpeed;
}

double PlayerCube::getSpeed() {
    return speed;
}

bool PlayerCube::setDirection(int direction) {
    if(!actionRunning) {
        angle = 0;
        startTime = glutGet(GLUT_ELAPSED_TIME);
        actionRunning = true;
        forwardDir = 0;
        sideDir = 0;
        switch(direction) {
            case 1:
                forwardDir = 1;
                break;
            case 2:
                sideDir = 1;
                break;
            case 3:
                forwardDir = -1;
                break;
            case 4:
                sideDir = -1;
                break;
        }
        return true;
    }
    return false;
}

void PlayerCube::render(double cameraX, double cameraY, double cameraZ) {
    double t = speed * (glutGet(GLUT_ELAPSED_TIME) - startTime) / 1000.0;
    double a = 0;
    if(actionRunning) {
        if(t > 1) {
            actionRunning = false;
            a = 90;
            if(sideDir != 0) {
                posX += (sideDir * (1 - totalAdded));
            }
            if(forwardDir != 0) {
                posY += (-1 * forwardDir * (1 - totalAdded));
            }
            totalAdded = 0;
            posZ = baseZ;
        }
        else {
            a = t * 90.0;

            double vOffset = .71 * sin(radianFactor * (a + 45));
            if(t > 0.5) {
                vOffset = .71 * cos(radianFactor * (a - 45));
            }
            vOffset -= .5;

            posZ = vOffset + baseZ;
            if(sideDir != 0) {
                posX += (sideDir * (t - totalAdded));
                totalAdded = t;
            }
            if(forwardDir != 0) {
                posY += (-1 * forwardDir * (t - totalAdded));
                totalAdded = t;
            }
        }
    }

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    glColor3d(r, g, b);

    glPushMatrix();
        glTranslated(posX + cameraX, posY + cameraY, posZ + cameraZ);
        glRotated(a, forwardDir, sideDir, 0);
        glutSolidCube(1);
    glPopMatrix();
}
