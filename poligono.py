# -*- coding: utf-8 -*-
"""
Created on 13 Driadan 2022

@author: R. Pena Spinelli
"""

import math
import random as rd
import matplotlib.pyplot as plt

def scaleFactor(n): #Calculates the Sierpinski Scale Factor for the N-Gon
    i = int(n/4)
    sum = 0
    for k in range(1,i+1):
        sum += math.cos(2*math.pi*k/n)
    return 1/(2*(1+sum))

#### Functions for Polar Vectors algebra ####
def addPolarVectors(p1, p2):
    r1, theta1 = p1
    r2, theta2 = p2
    r = math.sqrt(r1**2 + r2**2 + 2*r1*r2*math.cos(theta2 - theta1))
    theta = theta1 + math.atan2(r2*math.sin(theta2 - theta1),
                                r1 + r2*math.cos(theta2 - theta1))
    return [r, theta]

def subtractPolarVectors(p1, p2):
    p2 = [p2[0],p2[1] + math.pi]
    return addPolarVectors(p1, p2)

def scalePolarVector(p, alpha):
    return [p[0]*alpha, p[1]]

##### Insert Parameters #####
n = 4
points = 100000

######### Plot Setup #########
fig = plt.figure()
ax = fig.add_subplot(projection='polar')
ax.set_theta_zero_location('N')
plt.axis('off')
fig.tight_layout()

####### Points & Math ########    
ratio = scaleFactor(n)

V = []
for i in range(n): #generates the vertex points
    v = (1, i*2*math.pi/n) # vertex = (r, theta)
    V.append(v)

if n==4: # The Sierpinski Square is very dull. So make the Sierpinski carpet instead
    n = 8
    ratio = 1/3
    V = []
    for i in range(8): #generates the vertex points
        v = (1, i*2*math.pi/n) # vertex = (r, theta)
        if i%2 != 0:
            v = scalePolarVector(v, math.sqrt(2)/2)
        V.append(v)

for v in V: #plot vertex points
    ax.scatter(v[1], v[0], s=100, marker='.', c='k')

p = [1, 0] #starting point p[r, theta]
#ax.scatter(p[1], p[0], s=50, marker='.', c='r')

listaR = []
listaTheta = []

for i in range(points):
    v = V[rd.randint(0, n-1)]
    #v = V[0]
    p = addPolarVectors(
            scalePolarVector(
                subtractPolarVectors(v, p),
            -ratio),
        v)
    listaR.append(p[0])
    listaTheta.append(p[1])
ax.scatter(listaTheta, listaR, s=1, marker='.', c='b')
