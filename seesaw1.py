from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import time

wsize=1000
theta=0
x=200
y=0
DIR=1
coordinate=[[0,0],[300,300]]

def triangle():
    glColor3f(1,0,0)
    glBegin(GL_POLYGON)
    glVertex2f(0,0)
    glVertex2f(-50,-100)
    glVertex2f(50,-100)
    glEnd()
    glFlush()

def seesaw(x,y,theta):
    glColor3f(1,0,0)
    glLineWidth(5)
    glBegin(GL_LINES)
    glVertex2f(x*math.cos(math.radians(theta))-y*math.sin(math.radians(theta)), x*math.sin(math.radians(theta))+y*math.cos(math.radians(theta)))
    glVertex2f(-x*math.cos(math.radians(theta))-y*math.sin(math.radians(theta)),-x*math.sin(math.radians(theta))+y*math.cos(math.radians(theta)))
    glEnd()
    glFlush()



def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    triangle()
    seesaw(x,y,theta)
    glutSwapBuffers()

def animate(temp):
    global theta,DIR
    glutPostRedisplay()
    glutTimerFunc(int(1000/60),animate,int(0))
    if(theta>=20):
        DIR=0
    if(theta<-20):
        DIR=1
    if(DIR==1):
        theta+=0.1
    else:
        theta-=0.1
    
    



def main():
    glutInit()
    glutInitWindowSize(wsize,wsize)
    glutInitWindowPosition(0,0)
    glutCreateWindow("seesaw")
    glutDisplayFunc(draw)
    glutTimerFunc(0,animate,0)
    glClearColor(0,0,0,0)
    gluOrtho2D(-wsize,wsize,-wsize,wsize)
    glutMainLoop()
main()