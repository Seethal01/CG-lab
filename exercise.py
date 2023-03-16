from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

wsize=1000
x=0
y=0
theta=0
dir=1
coordinate=[[0,0],[100,100]]

def rectangle():
    global x,y,theta,dir,coordinate
    glColor3f(1,1,0)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(0,0)
    glVertex2f(100,0)
    glVertex2f(100,500)
    glVertex2f(0,500)
    glEnd()
    glFlush()
    glColor3f(1,0,0)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(0,-250)
    glVertex2f(0,0)
    glVertex2f(45,0)
    glVertex2f(45,-250)
    glEnd()
    glFlush()
    glColor3f(1,0,0)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(55,-250)
    glVertex2f(55,0)
    glVertex2f(100,0)
    glVertex2f(100,-250)
    glEnd()
    glFlush()
    glColor3f(1,0,0)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(0,350)
    glVertex2f(0,400)
    glVertex2f((-250+x)*math.cos(theta)+(350+y)*math.sin(theta) , -(250+x)*math.sin(theta)+(350+y)*math.cos(theta))
    glVertex2f((-250+x)*math.cos(theta)+(400+y)*math.sin(theta) , -(250+x)*math.sin(theta)+(400+y)*math.cos(theta))
    glEnd()
    glFlush()
    glColor3f(1,0,0)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(100,350)
    glVertex2f(100,400)
    glVertex2f((320+x)*math.cos(theta)-(350+y)*math.sin(theta),(320+x)*math.sin(theta)-(350+y)*math.cos(theta))
    glVertex2f((320+x)*math.cos(theta)-(400+y)*math.sin(theta),(320+x)*math.sin(theta)-(400+y)*math.cos(theta))
    glEnd()
    glFlush()
def circle():
    r=70
    x1=20
    y1=510
    glColor3f(1,0,0)
    glBegin(GL_TRIANGLE_FAN)
    for i in range(0,360,1):
        x1=r*math.cos(i)+x1
        y1=r*math.sin(i)+y1
        glVertex2f(x1,y1)
    glEnd()
    glFlush()
        
def draw():
    global x,y,theta
    glClear(GL_COLOR_BUFFER_BIT)
    rectangle()
    circle()
    glutSwapBuffers()

def animate(temp):
    global x,y,theta,dir
    glutPostRedisplay()
    glutTimerFunc(int(1000/60),animate,int(0))
    
def main():
    glutInit()
    glutInitWindowSize(wsize,wsize)
    glutInitWindowPosition(0,0)
    glutCreateWindow("Exercising")
    glutDisplayFunc(draw)
    glutTimerFunc(0,animate,0)
    glClearColor(1,1,1,1)
    gluOrtho2D(-wsize,wsize,-wsize,wsize)
    glutMainLoop()
main()