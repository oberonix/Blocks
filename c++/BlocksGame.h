#include "GLHandler.h"
#include "PlayerCube.h"
#include <iostream>
using namespace std;

const double ZOOM_SPEED = .5;

class BlocksGame {
  private:
    PlayerCube* playerCube;
    int locX;
    int locY;
    double cameraX;
    double cameraY;
    double cameraZ;
    void updateCamera(void);
    static BlocksGame* instance;
    int **map;
    int mapHeight;
    int mapWidth;
    bool checkMove(int, int);
    void drawCube(double x, double y, double z, double r, double g, double b);
    void drawMap();
  public:
    static BlocksGame* inst();
    static void keyHandler(unsigned char key, int x, int y);
    static void resizeHandler(int width, int height);
    static void specialKeysHandler(int key, int x, int y);
    static void displayHandler(void);
    void run(int argc, char *argv[]);
    void display(void);
    void resize(int width, int height);
    void key(unsigned char key, int x, int y);
    void specialKeys(int key, int x, int y);
    ~BlocksGame();
};
