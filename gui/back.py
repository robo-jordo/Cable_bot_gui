#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as plt3d
from mpl_toolkits.mplot3d import Axes3D
import time
import io
import math
#678+114.3
class DrawCableBot:
    def __init__(self):
        self.length_list = [0, 0, 0, 0]
        self.length = 0.98
        self.width = 0.98
        self.heighth = 0.792
        self.posX = 0.49
        self.posY = 0.49
        self.posZ = 0.47
        self.XYZ = np.array([[0, 0, 0],
                [self.length, 0, 0],
                [0, self.width, 0],
                [self.length, self.width, 0],
                [0, 0, self.heighth],
                [self.length, 0, self.heighth],
                [self.length, self.width, self.heighth],
                [0, self.width, self.heighth]])
        self.cables=[]

    def initializaton(self):
        # initialization

        self.fig = plt.figure()
        self.fig.set_size_inches(10, 10)
        self.ax = self.fig.add_subplot(111, projection='3d', aspect='equal')
        self.ax.view_init(azim=30)

    def drawNodes(self):
        # plot the nodes
        for x, y, z in self.XYZ:
            self.ax.scatter(x, y, z, color='black', marker='s')

    def drawLines(self):
        # plot the lines
        # draw rectangular
        lineOrder = [(0, 1), (1, 3), (3, 2), (2, 0),
                     (4, 5), (5, 6), (6, 7), (7, 4),
                     (0, 4), (1, 5), (2, 7), (3, 6)]
        for (p1, p2) in lineOrder:
            xs = (self.XYZ[p1][0], self.XYZ[p2][0])
            ys = (self.XYZ[p1][1], self.XYZ[p2][1])
            zs = (self.XYZ[p1][2], self.XYZ[p2][2])
            line = plt3d.art3d.Line3D(xs, ys, zs)
            self.ax.add_line(line)

    def drawGoal(self,delta=0.0):
        # draw cable and end effector
        self.ax.scatter(self.posX, self.posY, self.posZ, color='red', marker='s')
        NoCable=False
        if(len(self.cables)==0):
            NoCable=True
        else:
            for line in self.cables:
                line.remove()
        self.cables=[1,1,1,1]
        cableIndex=0
        for xyz in self.XYZ[4:8]:
            if cableIndex == 0:
                xs = (xyz[0], self.posX+delta)
                ys = (xyz[1], self.posY+delta)
            elif cableIndex == 1:
                xs = (xyz[0], self.posX+delta)
                ys = (xyz[1], self.posY+delta)
            elif cableIndex == 2:
                xs = (xyz[0], self.posX+delta)
                ys = (xyz[1], self.posY+delta)
            elif cableIndex == 3:
                xs = (xyz[0], self.posX+delta)
                ys = (xyz[1], self.posY+delta)
            zs = (xyz[2], self.posZ)
            lengthcal=round(lengthCal(xs,ys,zs,cableIndex),3)

            self.length_list[cableIndex]= lengthcal
            self.temporary = self.length_list

            self.ax.text(xyz[0],xyz[1],xyz[2],  '%s' % (str(lengthcal)), size=20, zorder=1,  color='k')
            line = plt3d.art3d.Line3D(xs, ys, zs)
            self.cables[cableIndex]=line
            self.ax.add_line(self.cables[cableIndex])
            cableIndex=cableIndex+1
        # self.temporary = self.length_list[3]
        # self.length_list[3] = self.length_list[2]
        # self.length_list[2] = self.temporary
        return self.length_list


    def setPos(self,x,y,z):
        self.posX=x
        self.posY=y
        self.posZ=z

def lengthCal(xs,ys,zs,cableIndex):
    cablelength=math.sqrt((xs[0]-xs[1])**2+(ys[0]-ys[1])**2+(zs[0]-zs[1])**2)
    print('Length of Cable',cableIndex,'is:', cablelength)
    return cablelength

if __name__ == '__main__':
    buff = io.BytesIO()
    dcb = DrawCableBot()
    dcb.initializaton()
    dcb.drawNodes()
    dcb.drawLines()
    goalX, goalY, goalZ = input("Enter goal position here: ").split()
    goalX=float(goalX)
    goalY=float(goalY)
    goalZ=float(goalZ)
    dcb.drawGoal()
    #plt.pause(0.5)
    # time.sleep(2)
    goalPos=(goalX, goalY, goalZ)
    print(goalPos)
    originPos=(dcb.posX,dcb.posY,dcb.posZ)
    num =10
    deltax=(goalPos[0]-originPos[0])/num
    deltay=(goalPos[1]-originPos[1])/num
    deltaz=(goalPos[2]-originPos[2])/num

    for i in range(0,num+1):
        x = deltax*i+originPos[0]
        y = deltay*i+originPos[1]
        z = deltaz*i+originPos[2]
        dcb.setPos(x,y,z)
        dcb.drawGoal()
        plt.pause(0.5)
        plt.savefig("traj.png")

    plt.show()
