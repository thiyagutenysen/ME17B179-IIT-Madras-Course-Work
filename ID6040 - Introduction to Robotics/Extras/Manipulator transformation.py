# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 18:41:47 2020

@author: chella
"""
from sympy import symbols
from sympy import Matrix
from sympy import sin,cos,eye
import math

n=int(input(" send in the number of dh parameters = "))
theta=symbols('theta0:%d'%n)
d=symbols('d0:%d'%n)
a=symbols('a0:%d'%n)
alpha=symbols('alpha0:%d'%n)
thetas=[0]*n
ds=[0]*n
ass=[0]*n
alphas=[0]*n
str_flag=0
print(" Give all dh params one by on in (theta, d, a, alpha) order row by row ")
print() 
for i in range(n):
    test=input()
    try:
        thetas[i]=math.radians(float(test))
    except:
        thetas[i]=test
        str_flag+=1
    test=input()
    try:
        ds[i]=float(test)
    except:
        ds[i]=test
        str_flag+=1
    ass[i]=float(input())
    alphas[i]=math.radians(float(input()))

matrix=[0]*n
for i in range(n):
    matrix[i]=Matrix([[cos(theta[i]), -cos(alpha[i])*sin(theta[i]),  sin(alpha[i])*sin(theta[i]), a[i]*cos(theta[i])],
                      [sin(theta[i]),  cos(alpha[i])*cos(theta[i]), -sin(alpha[i])*cos(theta[i]), a[i]*sin(theta[i])],
                      [0.0,            sin(alpha[i]),                cos(alpha[i]),               d[i]              ],
                      [0.0,            0.0,                          0.0,                         1.0               ]])

Final_matrix=eye(4,4)

for i in range(n):
    Final_matrix=Final_matrix*matrix[i]

print(Final_matrix)
print()

# substitution
for i in range(4):
    replacements1=[(theta[i], thetas[i]) for i in range(n)]
    replacements2=[(d[i], ds[i]) for i in range(n)]
    replacements3=[(a[i], ass[i]) for i in range(n)]
    replacements4=[(alpha[i], alphas[i]) for i in range(n)]
final=Final_matrix.subs(replacements1+replacements2+replacements3+replacements4)


if str_flag==0:
    for i in range(16):
        final[i]=round(final[i],4)
        
print(final)



    