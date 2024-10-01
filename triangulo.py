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

p1 = (-0.5, 0)
p2 = (0.5, 0)
p3 = (0, math.sqrt(3)/2)

Vertices = [p1, p2, p3]
for ponto in Vertices:
    plt.plot(ponto[0], ponto[1], markersize=10, marker='.', c='k')

x = 0
y = math.sqrt(3)/6
plt.plot(x, y, markersize=1, marker='.', c='b')


n = 30000
for i in range(n):
    vertice = Vertices[rd.randint(0,2)]
    #vertice = Vertices[0]
    x = (vertice[0]+x)/2
    y = (vertice[1]+y)/2
    plt.plot(x, y, markersize=1, marker='.', c='b')


"""

n = 3
for i in range(n):
    plt.plot(x, y, markersize=3, marker='.', c='b')
    #vertice = Vertices[rd.randint(0,2)]
    vertice = Vertices[0]
    x = (vertice[0]+x)/2
    y = (vertice[1]+y)/2


for i in range(n):
    plt.plot(x, y, markersize=3, marker='.', c='b')
    #vertice = Vertices[rd.randint(0,2)]
    vertice = Vertices[1]
    x = (vertice[0]+x)/2
    y = (vertice[1]+y)/2


for i in range(n):
    plt.plot(x, y, markersize=3, marker='.', c='b')
    #vertice = Vertices[rd.randint(0,2)]
    vertice = Vertices[2]
    x = (vertice[0]+x)/2
    y = (vertice[1]+y)/2
    
    
    
for i in range(n):
    plt.plot(x, y, markersize=3, marker='.', c='r')
    #vertice = Vertices[rd.randint(0,2)]
    vertice = Vertices[0]
    x = (vertice[0]+x)/2
    y = (vertice[1]+y)/2

for i in range(n):
    plt.plot(x, y, markersize=3, marker='.', c='r')
    #vertice = Vertices[rd.randint(0,2)]
    vertice = Vertices[1]
    x = (vertice[0]+x)/2
    y = (vertice[1]+y)/2

for i in range(n):
    plt.plot(x, y, markersize=3, marker='.', c='r')
    #vertice = Vertices[rd.randint(0,2)]
    vertice = Vertices[2]
    x = (vertice[0]+x)/2
    y = (vertice[1]+y)/2
    
    

for i in range(n):
    plt.plot(x, y, markersize=3, marker='.', c='k')
    #vertice = Vertices[rd.randint(0,2)]
    vertice = Vertices[0]
    x = (vertice[0]+x)/2
    y = (vertice[1]+y)/2

for i in range(n):
    plt.plot(x, y, markersize=3, marker='.', c='k')
    #vertice = Vertices[rd.randint(0,2)]
    vertice = Vertices[1]
    x = (vertice[0]+x)/2
    y = (vertice[1]+y)/2

for i in range(n):
    plt.plot(x, y, markersize=3, marker='.', c='k')
    #vertice = Vertices[rd.randint(0,2)]
    vertice = Vertices[2]
    x = (vertice[0]+x)/2
    y = (vertice[1]+y)/2




plt.plot(x, y, markersize=3, marker='.', c='b')
"""