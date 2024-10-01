# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 21:12:42 2022

@author: R. Pena Spinelli
"""

import math
import random as rd
import matplotlib.pyplot as plt

plt.clf()
plt.axis('equal')

p1 = (  -0.5,   -0.5)
p2 = (  0,      -0.5)
p3 = (  0.5,    -0.5)
p4 = (  0.5,    0)
p5 = (  0.5,    0.5)
p6 = (  0,      0.5)
p7 = (  -0.5,   0.5)
p8 = (  -0.5,   0)

Vertices = [p1, p2, p3, p4, p5, p6, p7, p8]
for ponto in Vertices:
    plt.plot(ponto[0], ponto[1], markersize=10, marker='.', c='k')

x = 0
y = 0
plt.plot(x, y, markersize=1, marker='.', c='b')


n = 100000
for i in range(n):
    vertice = Vertices[rd.randint(0,7)]
    #vertice = Vertices[0]
    x = (vertice[0]-x)*2/3 + x
    y = (vertice[1]-y)*2/3 + y
    plt.plot(x, y, markersize=1, marker='.', c='b')