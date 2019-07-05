#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Se definen las ecuaciones de Lorenz
def lorenz(x, y, z, s=10, r=28, b=2.667):
    X = s*(y - x)
    Y = r*x - y - x*z
    Z = x*y - b*z
    return X, Y, Z

#Se define el tiempo
dt = 0.01
paso = 5000


xs = np.empty((paso + 1,))
ys = np.empty((paso + 1,))
zs = np.empty((paso + 1,))

# Valores iniciales
xs[0], ys[0], zs[0] = (0.0, 1.0, 0.0)
t = [0]

#print(xs,ys,zs)
for i in range(0, paso):
# Derivamos
    X, Y, Z = lorenz(xs[i], ys[i], zs[i])
    xs[i + 1] = xs[i] + (X * dt)
    ys[i + 1] = ys[i] + (Y * dt)
    zs[i + 1] = zs[i] + (Z * dt)
    t.append(t[i]+dt)
    
    #print ("x=",xs,"y=",ys,"z=",zs) #Valores resueltos de x, y, z
    
#Gráficas en 2D   


plt.figure()
plt.plot(t,ys)
plt.title("Atractor de Lorentz t vs y")
plt.grid(color='B', linestyle='-', linewidth=0.1)
plt.xlabel('Eje t')
plt.ylabel('Eje Y')


plt.figure()
plt.title("Atractor de Lorentz x vs z")
plt.plot(xs,zs)
plt.grid(color='B', linestyle='-', linewidth=0.1)
plt.xlabel('Eje X')
plt.ylabel('Eje Z')

plt.figure()
plt.title("Atractor de Lorentz z vs x")
plt.plot(zs,xs)
plt.grid(color='B', linestyle='-', linewidth=0.1)
plt.xlabel('Eje Z')
plt.ylabel('Eje X')



#Gráfica en 3D 

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.set_title("Atractor de Lorentz")
ax.plot(xs, ys, zs, lw=0.8)
ax.set_xlabel("X ")
ax.set_ylabel("Y ")
ax.set_zlabel("Z ")


plt.show()


# In[ ]:




