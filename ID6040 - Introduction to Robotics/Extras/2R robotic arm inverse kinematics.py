# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 17:33:02 2020

@author: chella
"""
import math
import sys

l1=float(input(" give length of link 1: "))
l2=float(input(" give length of link 2: "))
print()
print(" Give input of final position matris one by one")
final_pos_matrix = [[float(input()) for x in range (4)] for y in range(4)] 

px=final_pos_matrix[0][3]
py=final_pos_matrix[1][3]

cos2=px**2+py**2-l1**2-l1**2
sin2=(1-cos2**2)**0.5

#theta2=math.atan2(sin2,cos2)
try:
   theta2=math.atan2(sin2,cos2)
except :
   print("Position can't be attained")
   sys.exit()
theta2=math.atan2(sin2,cos2)
r=l1*math.cos(theta2)+l2
s=l1*math.sin(theta2)

theta1=math.atan2(r*py-s*px, r*px+s*py)

print("Theta1: ",math.degrees(theta1), "theta2: ",math.degrees(theta2))