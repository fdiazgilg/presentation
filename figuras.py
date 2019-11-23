import turtle
import pygame

t = turtle.Turtle()

def poligono(num_lados):
    for r in range(num_lados):
        t.forward(40)
        t.left(360/num_lados)



