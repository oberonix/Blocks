#include "BlocksGame.h"

BlocksGame* BlocksGame::instance = NULL;

BlocksGame* BlocksGame::inst() {
    if(instance == NULL) {
        instance = new BlocksGame();
    }
    return instance;
}

void BlocksGame::keyHandler(unsigned char key, int x, int y) {
    instance->key(key, x, y);
}

void BlocksGame::resizeHandler(int width, int height) {
    instance->resize(width, height);
}

void BlocksGame::specialKeysHandler(int key, int x, int y) {
    instance->specialKeys(key, x, y);
}

void BlocksGame::displayHandler(void) {
    instance->display();
}


void BlocksGame::run(int argc, char *argv[]) {
    mapHeight = 10;
    mapWidth = 10;

    map = new int*[mapHeight];
    for (int i = 0; i < mapHeight; ++i) {
        map[i] = new int[mapWidth];
        for (int j = 0; j < mapWidth; j++) {
            if(i == 5 && j == 5) {
                map[i][j] = 0;
            }
            else if (i == 0 || j == 0 || i == mapHeight - 1 || j == mapWidth - 1) {
                map[i][j] = 2;
            }
            else {
                map[i][j] = 1;
            }
        }
    }



    //init opengl/glut
    GLHandlerInit(argc, argv);

    //setup window
    glutInitWindowSize(1024, 600);
    glutInitWindowPosition(0, 0);
    GLHandlerDisplayInit();
    glutCreateWindow("Blocks");

    //set handlers
    glutReshapeFunc(BlocksGame::resizeHandler);
    glutDisplayFunc(BlocksGame::displayHandler);
    glutKeyboardFunc(BlocksGame::keyHandler);
    glutSpecialFunc(BlocksGame::specialKeysHandler);

    GLHandlerFinishInit();

    //init gamestate
    locX = 3;
    cameraX = 3;
    locY = 1;
    cameraY = locY;
    playerCube = new PlayerCube(locX, -1 * locY);
    playerCube->setSpeed(5);

    //start game loop
    glutMainLoop();
}

void BlocksGame::display(void) {
    playerCube->render(0, 0, 0);
    drawMap();
    updateCamera();

    glutSwapBuffers();
}

void BlocksGame::updateCamera(void) {
    double x = playerCube->getX() - cameraX;
    double y = playerCube->getY() - cameraY;
    cameraX = playerCube->getX();
    cameraY = playerCube->getY();
    gluLookAt(x, y, 0, x, y, -6, 0, 1, 0);
}

void BlocksGame::drawCube(double x, double y, double z, double r, double g, double b) {
    glColor3d(r, g, b);
    glPushMatrix();
        glTranslated(x, y, z);
        glutSolidCube(1);
    glPopMatrix();
}

void BlocksGame::drawMap() {
    double z = -7;
    double color = 0;

    for (int i = 0; i < mapHeight; ++i) {
        for (int j = 0; j < mapWidth; j++) {
            bool draw = map[i][j] == 1;
            if(map[i][j] == 2) {
                draw = true;
                double altColor = color == 0 ? 1 : 0;
                drawCube(j, -1 * i, z + 1, altColor, altColor, altColor);
            }
            if(draw) {
                drawCube(j, -1 * i, z, color, color, color);
            }
            color = color == 0 ? 1 : 0;
        }
        if(mapWidth % 2 == 0) {
            color = color == 0 ? 1 : 0;
        }
    }
}

void BlocksGame::resize(int width, int height) {
    const float ar = (float) width / (float) height;

    glViewport(0, 0, width, height);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    glFrustum(-ar, ar, -1.0, 1.0, 2.0, 100.0);
    gluLookAt(0 + cameraX, -5 + cameraY, 0, cameraX, cameraY, -6, 0, 1, 0);

    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
}

void BlocksGame::key(unsigned char key, int x, int y) {
    switch (key)
    {
        case 27 :
            exit(0);
            break;
        case 'q':
            playerCube->setColor(0, 1, 0);
            break;
        case 'w':
            playerCube->setColor(1, 0, 0);
            break;
        case 'e':
            playerCube->setColor(0, 0, 1);
            break;
        case 'r':
            playerCube->setColor(1, 1, 0);
            break;
        case 'u':
            playerCube->setSpeed(playerCube->getSpeed() + 1);
            break;
        case 'j':
            playerCube->setSpeed(playerCube->getSpeed() - 1);
            break;
        case 'y':
            cameraZ -= ZOOM_SPEED;
            break;
        case 'h':
            cameraZ += ZOOM_SPEED;
            break;
    }
    glutPostRedisplay();
}

BlocksGame::~BlocksGame() {
    for (int i = 0; i < mapHeight; ++i) {
        delete [] map[i];
    }
    delete [] map;
}

bool BlocksGame::checkMove(int x, int y) {
    //boundary check
    if(x < 0 || y < 0 || y >= mapHeight || x >= mapWidth) {
        return false;
    }
    if(map[y][x] == 1) {
        return true;
    }
    return false;
}

void BlocksGame::specialKeys(int key, int x, int y) {
    switch (key) {
        case GLUT_KEY_LEFT:
            if(checkMove(locX - 1, locY)) {
                if(playerCube->setDirection(4)) {
                    locX--;
                }
            }
            break;
        case GLUT_KEY_RIGHT:
            if(checkMove(locX + 1, locY)) {
                if(playerCube->setDirection(2)) {
                    locX++;
                }
            }
            break;
        case GLUT_KEY_DOWN:
            if(checkMove(locX, locY + 1)) {
                if(playerCube->setDirection(1)) {
                    locY++;
                }
            }
            break;
        case GLUT_KEY_UP:
            if(checkMove(locX, locY - 1)) {
                if(playerCube->setDirection(3)) {
                    locY--;
                }
            }
            break;
    }
}
