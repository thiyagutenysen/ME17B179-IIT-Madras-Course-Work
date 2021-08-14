# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 22:31:45 2020

@author: chella
"""

from sympy import symbols
from sympy import Matrix
from sympy import sin,cos,eye
import math
from sympy.vector import CoordSys3D,matrix_to_vector
N = CoordSys3D('N')

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
    test=input()
    try:
        ass[i]=float(test)
    except:
        ass[i]=test
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
    
def get_position(joint):
    intermediate=eye(4,4)
    if joint==0:
        b=Matrix([0,0,1])
        b = matrix_to_vector(b, N)
        dist=(Final_matrix).col(3)
        dist.row_del(3)
        dist = matrix_to_vector(dist, N)
    else:
        for i in range(joint):
            intermediate=intermediate*matrix[i]
        #print(intermediate,"heeeeeee")
        b=intermediate.col(2)
        #print(b,"hooooooooo")
        b.row_del(3)
        #print(b,"haaaaaaaa")
        b = matrix_to_vector(b, N)
        dist=(Final_matrix-intermediate).col(3)
        dist.row_del(3)
        #print("Dissssssssssst",i,dist)
        dist = matrix_to_vector(dist, N)
    return b,dist # sending vectors

j=[0]*n
for i in range(n):
    b,dist=get_position(i)
    #print(dist,"diiiiiiiiiiiiiist")
    position_jacobian=b.cross(dist)
    #print(position_jacobian,"posssssss")
    if type(thetas[i])!=str:
        position_jacobian=b
        orientation_jacobian=0*N.i+ 0*N.j+ 0*N.k
    else:
        orientation_jacobian=b
        position_jacobian=b.cross(dist)
    #print(orientation_jacobian,"orrrrrrrrr")
    position_jacobian=position_jacobian.to_matrix(N)
    #print(position_jacobian,"posiiiiiiiiii")
    orientation_jacobian=orientation_jacobian.to_matrix(N)
    #print(orientation_jacobian,"orienttttttttttt",orientation_jacobian.shape)
    #position_jacobian=position_jacobian.T
    #orientation_jacobian=orientation_jacobian.T
    j[i]=position_jacobian.row_insert(3,orientation_jacobian)
    #print(j[i],j[i].shape,"jjjjjjjjjjjjjjjj")
#print(j[0],j[1].shape)
jacobian=Matrix()
for i in range(n):
    jacobian=jacobian.col_insert(i,j[i])
    #print(jacobian, "1111111111111111111111111111111111111",jacobian.shape)  
#print("Jaaaaaccccoooooooooooooobbbbbiiiaaaaaaaaaan",jacobian,jacobian.shape) # in symbolic form
    
# substitution
replacements1=[(theta[i], thetas[i]) for i in range(n)]
replacements2=[(d[i], ds[i]) for i in range(n)]
replacements3=[(a[i], ass[i]) for i in range(n)]
replacements4=[(alpha[i], alphas[i]) for i in range(n)]
final=jacobian.subs(replacements1+replacements2+replacements3+replacements4)

print()
if str_flag==0:
    for i in range(16):
        final[i]=round(final[i],4)
        
print("waaaaaalaaaaaa",final) # in numeric form