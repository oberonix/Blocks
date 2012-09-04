#include "GLHandler.h"
#define _USE_MATH_DEFINES
#include <math.h>
#include <iostream>
const double radianFactor = M_PI / 180;

class PlayerCube {
  private:
    double angle;
    int sideDir;
    int forwardDir;
    double startTime;
    bool actionRunning;
    double posX;
    double posY;
    double baseZ;
    double posZ;
    double totalAdded;
    double r;
    double g;
    double b;
    double speed;
  public:
    PlayerCube(double, double);
    void render(double, double, double);
    void setColor(double, double, double);
    bool setDirection(int);
    void setSpeed(double);
    double getSpeed();
    double getX();
    double getY();
};
