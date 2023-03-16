from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

wsize=1000


def draw_triangle():
    global x1,x2,x3,y1,y2,y3
    x1=float(input("Enter x1:"))
    x2=float(input("Enter x2:"))
    x3=float(input("Enter x3:"))
    y1=float(input("Enter y1:"))
    y2=float(input("Enter y2:"))
    y3=float(input("Enter y3:"))
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1,0,0)
    glPointSize(5)
    glBegin(GL_TRIANGLES)
    glVertex2f(x1,y1)
    glVertex2f(x2,y2)
    glVertex2f(x3,y3)
    glEnd()
    glFlush()

def translate():
    draw_triangle()
    xinc=float(input("change in x:"))
    yinc=float(input("change in y:"))
    glColor3f(0,1,0)
    glPointSize(5)
    glBegin(GL_TRIANGLES)
    glVertex2f(x1+xinc,y1+yinc)
    glVertex2f(x2+xinc,y2+yinc)
    glVertex2f(x3+xinc,y3+yinc)
    glEnd()
    glFlush()

def rotate():
    draw_triangle()
    deg=int(float("angle to be rotated(degree)?"))
    angle=(3.14/180)*deg
    glColor3f(0,1,0)
    glPointSize(5)
    glBegin(GL_TRIANGLES)
    glVertex2f(x1*math.cos(angle)-y1*math.sin(angle) , x1*math.sin(angle)+y1*math.cos(angle))
    glVertex2f(x2*math.cos(angle)-y2*math.sin(angle) , x2*math.sin(angle)+y2*math.cos(angle))
    glVertex2f(x3*math.cos(angle)-y3*math.sin(angle) , x3*math.sin(angle)+y3*math.cos(angle))
    glEnd()
    glFlush()

def scale():
    draw_triangle()
    scalex=float(input("enter x scale:"))
    scaley=float(input("enter y scale:"))
    glColor3f(0,1,0)
    glPointSize(5)
    glBegin(GL_TRIANGLES)
    glVertex2f(x1*scalex,y1*scaley)
    glVertex2f(x2*scalex,y2*scaley)
    glVertex2f(x3*scalex,y3*scaley)
    glEnd()
    glFlush()

def reflect():
    draw_triangle()
    glColor3f(0,1,0)
    glPointSize(5)
    case=int(input("Enter 1.about x axis\n2.about y axis\n3 about origin\n4 about x=y\n5 about x=-y"))
    if case==1:
        glBegin(GL_TRIANGLES)
        glVertex2f(x1,-y1)
        glVertex2f(x2,-y2)
        glVertex2f(x3,-y3)
        glEnd()
        
    elif case==2:
        glBegin(GL_TRIANGLES)
        glVertex2f(-x1,y1)
        glVertex2f(-x2,y2)
        glVertex2f(-x3,y3)
        glEnd()
        
    elif case==3:
        glBegin(GL_TRIANGLES)
        glVertex2f(-x1,-y1)
        glVertex2f(-x2,-y2)
        glVertex2f(-x3,-y3)
        glEnd()
      
    elif case==4:
        glBegin(GL_TRIANGLES)
        glVertex2f(y1,x1)
        glVertex2f(y2,x2)
        glVertex2f(y3,x3)
        glEnd()
        
    elif case==5:
        glBegin(GL_TRIANGLES)
        glVertex2f(-y1,-x1)
        glVertex2f(-y2,-x2)
        glVertex2f(-y3,-x3)
        glEnd()
    glFlush()

def shearing():
    draw_triangle()
    glColor3f(0,1,0)
    glPointSize(5)
    shx=float(input("Enter x shear:"))
    shy=float(input("Enter y shear:"))
    option=int(input("Enter 1.x shear\n 2.y shear\n 3.x=y shear"))
    if option==1:
        glBegin(GL_TRIANGLES)
        glVertex2f(x1+y1*shx,y1)
        glVertex2f(x2+y2*shx,y2)
        glVertex2f(x3+y3*shx,y3)
        glEnd()
    elif option==2:
        glBegin(GL_TRIANGLES)
        glVertex2f(x1,y1+x1*shy)
        glVertex2f(x2,y2+x2*shy)
        glVertex2f(x3,y3+x3*shy)
        glEnd()
    elif option==3:
        glBegin(GL_TRIANGLES)
        glVertex2f(x1+y1*shx,y1+x1*shy)
        glVertex2f(x2+y2*shx,y2+x2*shy)
        glVertex2f(x3+y3*shx,y3+x3*shy)
        glEnd()
    glFlush()

def main():
    glutInit()
    glutInitWindowSize(wsize,wsize)
    glutInitWindowPosition(0,0)
    glutCreateWindow("2d")
    choice=int(input("Enter 1.translation,2.rotation,3.scaling,4.reflection,5.shearing"))
    if choice==1:
        glutDisplayFunc(translate)
    elif choice==2:
        glutDisplayFunc(rotate)
    elif choice==3:
        glutDisplayFunc(scale)
    elif choice==4:
        glutDisplayFunc(reflect)
    elif choice==5:
        glutDisplayFunc(shearing)
    glClearColor(1,1,1,1)
    gluOrtho2D(-wsize,wsize,-wsize,wsize)
    glutMainLoop()
main()


