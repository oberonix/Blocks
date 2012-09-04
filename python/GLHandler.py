import OpenGL 
OpenGL.ERROR_ON_COPY = True 
from OpenGL.GL import *
from OpenGL.GLUT import *

light_ambient = GLfloat_4( 0.0, 0.0, 0.0, 1.0 )
light_diffuse = GLfloat_4( 1.0, 1.0, 1.0, 1.0 )
light_specular = GLfloat_4( 1.0, 1.0, 1.0, 1.0 )
light_position = GLfloat_4( 2.0, 5.0, 5.0, 0.0 )

mat_ambient = GLfloat_4( 0.7, 0.7, 0.7, 1.0 )
mat_diffuse = GLfloat_4( 0.8, 0.8, 0.8, 1.0 )
mat_specular = GLfloat_4( 1.0, 1.0, 1.0, 1.0 )
high_shininess = GLfloat_4( 100.0 )

def GLHandlerIdle() :
    glutPostRedisplay()

def GLHandlerInit(argv) :
    glutInit(argv)

def GLHandlerDisplayInit() :
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH)

def GLHandlerFinishInit() :
    glutIdleFunc(GLHandlerIdle)

    glClearColor(1,1,1,1)
    glEnable(GL_CULL_FACE)
    glCullFace(GL_BACK)

    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LESS)

    glEnable(GL_LIGHT0)
    glEnable(GL_NORMALIZE)
    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_LIGHTING)

    glLightfv(GL_LIGHT0, GL_AMBIENT,  light_ambient)
    glLightfv(GL_LIGHT0, GL_DIFFUSE,  light_diffuse)
    glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)

    glMaterialfv(GL_FRONT, GL_AMBIENT,   mat_ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE,   mat_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR,  mat_specular)
    glMaterialfv(GL_FRONT, GL_SHININESS, high_shininess)