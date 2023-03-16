from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import time
wsize = 1000
coordinate = [-400, 0]
theta=0

def display():
    global coordinate,theta
    glClear(GL_COLOR_BUFFER_BIT)
    ball()
    glFlush()
    coordinate[0] += 1
    coordinate[1] = 200*abs(math.sin(math.radians(theta)))
    theta+=1
    time.sleep(.007)

def ball():
    global coordinate

    for i in range(0, 361, 1):
        glBegin(GL_LINES)
        glColor3f(1, 0, 0)
        x, y = (50 * math.cos(math.radians(i)), 50 * math.sin(math.radians(i)))
        glVertex2f(coordinate[0] / wsize, coordinate[1] / wsize)
        glVertex2f((x + coordinate[0]) / wsize, ((y + coordinate[1]) / wsize))
        glEnd()


def main():
    glutInit()
    glutInitWindowSize(wsize, wsize)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("ball")
    glutDisplayFunc(display)
    glutIdleFunc(display)
    # gluOrtho2D(-wsize, wsize, -wsize, wsize)
    glutMainLoop()


main()
