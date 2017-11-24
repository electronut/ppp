"""
chaotic.py

Visualization of chaotic systems using the Turtle module.

Author: Mahesh Venkitachalam
Website: electronut.in

**********************
Python Playground Plus
**********************

Explorations in the spirit of my book Python Playground, No Starch Press, USA.

http://www.nostarch.com/pythonplayground
"""

import math
import turtle
import argparse

class Attractor:
    # constr
    def __init__(self, name, axes):
        self.name = name
        self.axes = axes
        self.scale = 1
        self.attrFunc = self.generateAttractor(name)

    # periodic update
    def update(self):
        x, y, z = self.attrFunc()
        #print(x, y)
        if self.axes == "xy":
            turtle.setpos(self.scale*x, self.scale*y)
        elif self.axes == "yz":
            turtle.setpos(self.scale*y, self.scale*z)
        else:
            turtle.setpos(self.scale*z, self.scale*x)
        turtle.pd()
        turtle.ontimer(self.update, 1)

    # generate the attractor function
    def generateAttractor(self, name):
        if name == "lorenz":
            # parameters
            P = 10
            A = 28
            B = 8.0/3.0
            dt = 0.01
            # initial conditions
            x = 1.0
            y = 1.0
            z = 1.0
            self.scale = 5
            def lorenz():
                nonlocal x, y, z
                x = x + dt*P*(y - x)
                y = y + dt*(x*(A - z) - y)
                z = z + dt*(x*y - B*z)
                return (x, y, z)
            return lorenz
        elif name == "thomas":
            # parameters
            b = 0.21
            # initial conditions
            x = 1.0
            y = 1.0
            z = 1.0
            dt = 0.1
            self.scale = 75
            def thomas():
                nonlocal x, y, z
                x = x + dt*(math.sin(y) - b*x)
                y = y + dt*(math.sin(z) - b*y)
                z = z + dt*(math.sin(x) - b*z)
                return (x, y, z)
            return thomas
        # invalid
        return None

def main():

    # set up arg parse
    parser = argparse.ArgumentParser(description="")
    # add expected arguments
    parser.add_argument('--axes', nargs=1, dest='axes', type=str, choices=["xy", "yz", "zx"], 
                        required=True, help="Axes: xy, yz, or zx")
                        
    parser.add_argument('--attr', nargs=1, dest='attr', type=str, choices=["lorenz", "thomas"], 
                        required=True, help="Attractor: thomas, lorenz")
    # parse args
    args = parser.parse_args()
 
    # set values
    axes = args.axes[0]
    name = args.attr[0]

    attractor = Attractor(name, axes)

    turtle.shape("turtle")
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("Strange Atrractors")

    turtle.color("white")
    turtle.pu()
    turtle.ontimer(attractor.update, 1)

    turtle.mainloop()

# call main
if __name__ == '__main__':
  main()
