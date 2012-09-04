import OpenGL
OpenGL.ERROR_ON_COPY = True
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from GLHandler import *

class GLRenderer :
    UP = GLUT_KEY_UP
    DOWN = GLUT_KEY_DOWN
    LEFT = GLUT_KEY_LEFT
    RIGHT = GLUT_KEY_RIGHT

    def __init(self) :
        pass
    
    def createWindow(self, argv, x, y, width, height, title, handler) :
        #init opengl/glut
        GLHandlerInit(argv)

        #setup window
        glutInitWindowSize(width, height)
        glutInitWindowPosition(x, y)
        GLHandlerDisplayInit()
        glutCreateWindow(title)

        #set handlers
        glutReshapeFunc(handler.resize)
        glutDisplayFunc(handler.display)
        glutKeyboardFunc(handler.key)
        glutSpecialFunc(handler.specialKeys)

        GLHandlerFinishInit()
    
    def loop(self) :
        glutMainLoop()
        
    def display(self) :
        glutSwapBuffers()
        
    def getElapsedTime(self) :
        return glutGet(GLUT_ELAPSED_TIME)
    
    def clear(self) :
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    def drawCube(self, r, g, b, x, y, z, angle = 0, xRot = 0, yRot = 0, zRot = 0) :
        glColor3d(r, g, b)
        glPushMatrix()
        glTranslated(x, y, z)
        if angle != 0 :
            glRotated(angle, xRot, yRot, zRot)
        glutSolidCube(1)
        glPopMatrix()
        
    def lookAt(self, eyeX, eyeY, eyeZ, centerX, centerY, centerZ, upX, upY, upZ) :
        gluLookAt(eyeX, eyeY, eyeZ, centerX, centerY, centerZ, upX, upY, upZ)
        
    def resize(self, width, height, camX, camY, camZ) :
        ar = width / height
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glFrustum(-ar, ar, -1.0, 1.0, 2.0, 100.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()