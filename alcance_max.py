import numpy as np
import matplotlib.pyplot as plt

def alcance_max(Vo,theta):
	g=9.8
	alcance_max= ((Vo**2)*2*np.abs(np.sin(theta))*np.abs(np.cos(theta)))/g
	return alcance_max

alpha = np.random.random()*10 + 35
theta = np.random.random()*np.pi/2

for i in range (1001):
	print i, alcance_max(alpha,theta)
	alpha = np.random.random()*10 + 35
	theta = np.random.random()*np.pi/2
	i = 1+i

























