from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

wsize=1000
x=0
y=0
dir=0
theta=0

def boat():
    global x,y
    glColor3f(0.1,0,0)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(0,0)
    glVertex2f(0,80)
    glVertex2f(450,80)
    glVertex2f(450,0) 
    glEnd()
    glFlush()
    glColor3f(0,0,0)
    glBegin(GL_TRIANGLES)
    glVertex2f(450,0)
    glVertex2f(450,80)
    glVertex2f(540,120)
    glEnd()
    glFlush()
    glColor3f(0,0,0)
    glBegin(GL_TRIANGLES)
    glVertex2f(0,0)
    glVertex2f(0,80)
    glVertex2f(-90,120)
    glEnd()
    glFlush()
    r=20
    x1=150
    y1=150
    glColor3f(1,0,0)
    glBegin(GL_TRIANGLE_FAN)
    for i in range(0,360,1):
        x1=r*math.cos(i)+x1
        y1=r*math.sin(i)+y1
        glVertex2f(x1,y1)
    glEnd()
    glFlush()
    glColor3f(0,0,0)
    glLineWidth(5)
    glBegin(GL_LINES)
    
    glVertex2f(160,80)
    glVertex2f(160,150)
    glEnd()
    glFlush()
    glColor3f(0,0,1)
    glLineWidth(10)
    glBegin(GL_LINES)
    glVertex2f(160,120)
    glVertex2f(x*math.cos(theta)+(y-180)*math.sin(theta),-x*math.sin(theta)+(y-180)*math.cos(theta))
    glEnd()
    glFlush()

def draw():
    global x,y
    glClear(GL_COLOR_BUFFER_BIT)
    boat()
    glutSwapBuffers()
    
def animate(temp):
    global x,y,theta,dir
    glutPostRedisplay()
    glutTimerFunc(int(1000/10),animate,int(0))
    if(theta<60):
        theta=theta+0.1
    else:
        theta=0
   



def main():
    glutInit()
    glutInitWindowSize(wsize,wsize)
    glutInitWindowPosition(0,0)
    glutCreateWindow("boat")
    glutDisplayFunc(draw)
    glutTimerFunc(0,animate,0)
    glClearColor(1,1,1,1)
    gluOrtho2D(-wsize,wsize,-wsize,wsize)
    glutMainLoop()
main()