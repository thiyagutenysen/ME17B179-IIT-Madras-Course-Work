# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 00:11:46 2020

@author: chella
"""

# Importing necessary headerfiles
from sympy import symbols, cos, sin, pi, simplify
import math
from sympy.matrices import Matrix

'''I am following Craig's convention, so the number of parameters
are a little different to what was done in class'''

# Creating symbols for joint variables
q1, q2, q3, q4, q5, q6 = symbols('q1:7')
d1, d2, d3, d4, d5, d6 = symbols('d1:7')
a0, a1, a2, a3, a4, a5 = symbols('a0:6')
alpha0, alpha1, alpha2, alpha3, alpha4, alpha5 = symbols('alpha0:6')

# DH Parameters
s = {alpha0:0,  a0:0, d1:0, q1:0,
     alpha1:0,  a1:1, d2:1, q2:0,
     alpha2:0,  a2:0, d3:0, q3:0,
     alpha3:0,  a3:0, d4:0, q4:0,
     alpha4:0,  a4:0, d5:0, q5:0,
     alpha5:0,  a5:0, d6:0, q6:0,}

#Homogeneous Transformation Matrices
T0_1 = Matrix([[             cos(q1),            -sin(q1),            0,              a0],
               [ sin(q1)*cos(alpha0), cos(q1)*cos(alpha0), -sin(alpha0), -sin(alpha0)*d1],
               [ sin(q1)*sin(alpha0), cos(q1)*sin(alpha0),  cos(alpha0),  cos(alpha0)*d1],
               [                   0,                   0,            0,               1]])
T1_2 = Matrix([[             cos(q2),            -sin(q2),            0,              a1],
               [ sin(q2)*cos(alpha1), cos(q2)*cos(alpha1), -sin(alpha1), -sin(alpha1)*d2],
               [ sin(q2)*sin(alpha1), cos(q2)*sin(alpha1),  cos(alpha1),  cos(alpha1)*d2],
               [                   0,                   0,            0,               1]])
T2_3 = Matrix([[             cos(q3),            -sin(q3),            0,              a2],
               [ sin(q3)*cos(alpha2), cos(q3)*cos(alpha2), -sin(alpha2), -sin(alpha2)*d3],
               [ sin(q3)*sin(alpha2), cos(q3)*sin(alpha2),  cos(alpha2),  cos(alpha2)*d3],
               [                   0,                   0,            0,               1]])
T3_4 = Matrix([[             cos(q4),            -sin(q4),            0,              a3],
               [ sin(q4)*cos(alpha3), cos(q4)*cos(alpha3), -sin(alpha3), -sin(alpha3)*d4],
               [ sin(q4)*sin(alpha3), cos(q4)*sin(alpha3),  cos(alpha3),  cos(alpha3)*d4],
               [                   0,                   0,            0,               1]])
T4_5 = Matrix([[             cos(q5),            -sin(q5),            0,              a4],
               [ sin(q5)*cos(alpha4), cos(q5)*cos(alpha4), -sin(alpha4), -sin(alpha4)*d5],
               [ sin(q5)*sin(alpha4), cos(q5)*sin(alpha4),  cos(alpha4),  cos(alpha4)*d5],
               [                   0,                   0,            0,               1]])
T5_6 = Matrix([[             cos(q6),            -sin(q6),            0,              a5],
               [ sin(q6)*cos(alpha5), cos(q6)*cos(alpha5), -sin(alpha5), -sin(alpha5)*d6],
               [ sin(q6)*sin(alpha5), cos(q6)*sin(alpha5),  cos(alpha5),  cos(alpha5)*d6],
               [                   0,                   0,            0,               1]])

''' To calculate a particular Transformation matrix,please substitute 
the DH parameters above and substitute the values.For example uncomment the line below'''
### Substituted_T0_1 = T0_1.subs(s)

'''For calculating the manipulator transformation matrix uncomment the codes below
 NOTE:This takes quite sometime for calculating without substituting first'''

### T0_6 = simplify(T0_1 * T1_2 * T2_3 * T3_4 * T4_5 * T5_6)
### print(T0_6)

'''For space coordinates and orientation of the tool tip uncomment the code below'''
### Space_coordinates_tooltip = T0_6[0:3][3]
### Orientation_tooltip = T0_6[0:3][0:3]

'''Using Puma Manipulator data from the tutorial quesion'''
s1 = {alpha0:0,  a0:0, d1:0,
      alpha1:-math.radians(90),  a1:0,
      alpha2:0, d3:0,
      alpha3:+math.radians(90),
      alpha4:-math.radians(90),  a4:0, d5:0,
      alpha5:+math.radians(90),  a5:0, d6:0}

T1_2 = T1_2.subs(s1)
print(T1_2)

T1_2 = T1_2.subs(s1)
T2_3 = T2_3.subs(s1)
T3_4 = T3_4.subs(s1)
T4_5 = T4_5.subs(s1)
T5_6 = T5_6.subs(s1)

T0_6 = simplify(T0_1 * T1_2 * T2_3 * T3_4 * T4_5 * T5_6)
print(T0_6)
