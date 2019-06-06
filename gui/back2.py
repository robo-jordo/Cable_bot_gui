#!/usr/bin/env python
import math 
W = 1
D = 1
X = 0
Y = 0
Z = 0

new_lengths = []

length_0 = math.sqrt((X)**2+(Y)**2+(Z)**2)
length_1 = math.sqrt((W-X)**2+(Y)**2+(Z)**2)
length_2 = math.sqrt((W-X)**2+(D-Y)**2+(Z)**2)
length_3 = math.sqrt((X)**2+(D-Y)**2+(Z)**2)


