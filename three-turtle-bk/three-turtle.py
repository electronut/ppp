"""
three-turtle.py

The Three Body Problem implemented in a simplistic way using Turtle Graphics.

Author: Mahesh Venkitachalam
Website: electronut.in
Python Playground Book: http://www.nostarch.com/pythonplayground
"""

import math
import turtle

xn, yn = (1, 1)

def henon():
    global xn, yn
    x = (yn + 1) - 1.4*xn*xn
    y = 0.3*xn
    xn, yn = x, y
    return (x, y)

def update():
    #x, y = fxy1()
    x, y = henon()
    #print(x, y)
    turtle.setpos(200*x, 200*y)
    turtle.pd()
    turtle.dot(5)
    turtle.pu()
    turtle.ontimer(update, 5)

def main():
    turtle.shape("turtle")
    turtle.color("blue")
    turtle.pu()
    turtle.ontimer(update, 1);

    turtle.mainloop()

# call main
if __name__ == '__main__':
  main()
