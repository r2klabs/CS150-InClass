# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 10:45:19 2020

@author: rkelley
"""

import turtle

def main():
    turtle.reset()
    turtle.penup()
    n = 5
    turtle.goto(-n**2 * 10/2,n**2 * 10/2)
    turtle.pendown()
    hilbert(n,90, 10)
    response = input("Press enter when done")
    turtle.done()
    
def hilbert(n, turn, distance):
    if n==1:
        turtle.forward(distance)
        turtle.right(turn)
        turtle.forward(distance)
        turtle.right(turn)
        turtle.forward(distance)
    else:
        turtle.right(turn)
        hilbert(n-1, -turn, distance)
        turtle.right(turn)
        turtle.forward(distance)
        hilbert(n-1, turn, distance)
        turtle.left(turn)
        turtle.forward(distance)
        turtle.left(turn)
        hilbert(n-1, turn, distance)
        turtle.forward(distance)
        turtle.right(turn)
        hilbert(n-1, -turn, distance)
        turtle.right(turn)
        
main()