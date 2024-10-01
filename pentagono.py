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

l = 1
a = math.tan(3*math.pi/10)*l/2
b = math.sin(2*math.pi/5)*l
c = math.cos(2*math.pi/5)*l
d = math.cos(math.pi/5)*l
h = a/math.sin(3*math.pi/10)

p1 = (0, 2*a+h)
p2 = (-2*d-l/2, a)
p3 = (-c-l, -h-b)
p4 = ( c+l, -h-b)
p5 = ( 2*d+l/2, a)

razao = 2*a/(2*a+h)

Vertices = [p1, p2, p3, p4, p5]
for ponto in Vertices:
    plt.plot(ponto[0], ponto[1], markersize=10, marker='.', c='k')

x = 0
y = 0
plt.plot(x, y, markersize=10, marker='.', c='b')


listaX = []
listaY = []

n = 4
for i in range(n):
    #vertice = Vertices[rd.randint(0,4)]
    vertice = Vertices[0]
    x = (vertice[0]-x)*razao + x
    y = (vertice[1]-y)*razao + y
    listaX.append(x)
    listaY.append(y)
    
plt.scatter(listaX, listaY, s=1, marker='.', c='b')


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