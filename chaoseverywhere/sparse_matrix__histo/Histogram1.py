import numpy as np
import matplotlib.pyplot as plt
MAX_ITER = 120 #necessarily less than 255
R=4
def mandelbrot(c):
    z=0
    i=0
    while i<MAX_ITER and abs(z)<=R:
        i+=1
        z=z**2+c
    if i==MAX_ITER:
        return 255
    else:
        return i

minx=-2
maxx=2
miny=-2
maxy=2
Nx=1024 #number of pixels height
Ny=1024 #number of pixels width
Nb_trait=16 #number of bars in the histogram, preferably a power of 2
haut_hist=10000 #to discretize the image of the histogram, the larger it is the more precise the histogram will be.
lgn_hist=Nb_trait
couleur0=(0.3,1,0.3)
couleur1=(0.3,0.3,1)
M=np.zeros([Ny,Nx])
N=np.zeros([haut_hist,lgn_hist,3])
im=np.zeros([Ny,Nx,3])
long_trait=256//Nb_trait
histogram={}

for i in range(Nb_trait):
    histogram[i]=0
for i in range(Ny):
    for j in range(Nx):
        x=minx+(maxx-minx)*j/Nx
        y=miny+(maxx-minx)*(Ny-i)/Ny
        c=x+y*1j
        M[i,j]=mandelbrot(c)
        histogram[M[i,j]//long_trait]+=1
im[:,:,0]=M/255*couleur1[0]+(1-M/255)*couleur0[0]
im[:,:,1]=M/255*couleur1[1]+(1-M/255)*couleur0[1]
im[:,:,2]=M/255*couleur1[2]+(1-M/255)*couleur0[2]
plt.figure(1)
plt.imshow(im)
plt.imsave("image.png",im)
plt.show()
s=max(histogram.values())
for j in range(lgn_hist):
    numbarre=(j*Nb_trait)//lgn_hist
    a=histogram[numbarre]/s
    for i in range(haut_hist):
        if i>haut_hist-1-np.floor(a*haut_hist):
            lamda=(numbarre+0.5)/Nb_trait
            N[i,j,0]=lamda*couleur1[0]+(1-lamda)*couleur0[0]
            N[i,j,1]=lamda*couleur1[1]+(1-lamda)*couleur0[1]
            N[i,j,2]=lamda*couleur1[2]+(1-lamda)*couleur0[2]
        else:
            N[i,j,0]=1
            N[i,j,1]=1
            N[i,j,2]=1
plt.figure(2)
plt.imshow(N, extent=[0,255,0,s], aspect=255/s)
plt.show()