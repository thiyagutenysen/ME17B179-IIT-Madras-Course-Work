# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 18:55:10 2020

@author: chella
"""
import math

# 4 axis SCARA bot inverse kinematics
final_pos=[]
print(" send in the final position transformation matrix one by one row wise ")
print()

for i in range(4):
    inputs=[]
    for j in range(4):
        inputs.append(float(input()))
    final_pos.append(inputs)
    
px=final_pos[0][3]
py=final_pos[1][3]
pz=final_pos[2][3]
nx=final_pos[0][0]
sx=final_pos[0][1]
a=425
b=375

s=(a**2-b**2+px**2+py**2)/(2*a)
t=px**2+py**2-a**2-b**2

theta11= math.degrees(math.atan2(py,px)+math.atan2(((px**2+py**2-s**2)**0.5),s))
theta12= math.degrees(math.atan2(py,px)+math.atan2(-((px**2+py**2-s**2)**0.5),s))
theta21=math.degrees(-math.atan2(((4*a**2*b**2)-t**2),t))
theta22=math.degrees(-math.atan2(-((4*a**2*b**2)-t**2),t))


theta1_2_4=math.degrees(math.atan2(sx,nx))

theta41=theta11-theta21-theta1_2_4
theta42=theta12-theta22-theta1_2_4
d3=777-pz


print(" values of variables are ", "theta1",theta11,"theta2",theta21,"d3",d3,"theta4",theta41)
print(" values of variables are ", "theta1",theta12,"theta2",theta22,"d3",d3,"theta4",theta42)
