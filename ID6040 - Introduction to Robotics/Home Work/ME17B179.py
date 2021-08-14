import numpy as np
print("Enter the transformation matrix of the end effector, one by one")

N = np.zeros([4,4])
for i in range(4):
	for j in range(4):
		N[i,j] = input()

q3 = 777 -int(N[2][3])

c2 = pow(int(N[0][3]),2) + pow(int(N[1][3]),2) - 375*375 - 425*425
s2 = pow(1-pow(c2,2),1/2)
q2 = np.arctan2(s2,c2)

r = 375*c2 + 425
s = 375*s2

q1 = np.arctan2(-1*r*int(N[1][3])-s*int(N[0][3]), int(N[0][3])*r -s*int(N[1][3]))
q4 = np.arctan2(-1*int(N[0][1]),int(N[0][0])) - q1 - q2

print("The joint variables are", q1*180/np.pi, " " ,q2*180/np.pi , " ", q3, " " ,q4*180/np.pi, " ")

