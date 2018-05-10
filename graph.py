import numpy as np
import matplotlib.pyplot as plt
import math

data_alc= np.loadtxt('alcance_max.txt')

x=data_alc[:,0]
y=data_alc[:,1]

g = 9.8
alpha = np.random.random(1000000)*10 + 35
theta = np.random.random(1000000)*2*np.pi

plt.figure()
count, bins, ignored =plt.hist(alpha, 50, normed=True, edgecolor = 'black',  linewidth=0.3)
plt.title('Vo')
plt.grid()
plt.savefig('Vel_ini.png')

plt.figure()
plt.title('Angulo*pi')
count, bins, ignored =plt.hist(theta, 8, normed=True, edgecolor = 'black',  linewidth=0.3, color= 'g')
plt.grid()
plt.savefig('Angulo.png')

def alcance_max(Vo,theta):
	g=9.8
	alcance_max= ((Vo**2)*2*np.sin(theta)*cos(theta))/g
	return alcance_max

plt.figure()
plt.title('Alcance maximo')
count, bins, ignored =plt.hist(y, 200, normed=True, edgecolor = 'black',  linewidth=0.3, color= 'g')
plt.xlabel('distance(m)')
plt.ylabel('Vo (m/s)')
plt.grid()
plt.savefig('alcance.png')




























