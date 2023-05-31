import matplotlib.pyplot as plt
import numpy as np
import math
# number of patches in both direction
m=13 # x
n=8 # y
# fit knots
r=0.5
theta= np.linspace(0,2*np.pi, m)
tt=np.reshape(np.tile(theta,(n,1)).T,(n*m))
phi= np.linspace(0, np.pi, n)
pp=np.reshape(np.tile(phi,(m,1)),(n*m))
x = r*np.sin(pp)*np.cos(tt)+(np.random.random((n*m))*2.0-1.0)*0.02
z = r*np.sin(pp)*np.sin(tt)+(np.random.random((n*m))*2.0-1.0)*0.02
y = r*np.cos(pp)+(np.random.random((n*m))*2.0-1.0)*0.02
for i in range(0,n):
    x[n*(m-1)+i]=x[i]
    y[n*(m-1)+i]=y[i]
    z[n*(m-1)+i]=z[i]  
for i in range(0,m):
    x[i*(n)]=0
    y[i*(n)]=r
    z[i*(n)]=0
    x[(i+1)*(n)-1]=0
    y[(i+1)*(n)-1]=-r
    z[(i+1)*(n)-1]=0
Px=np.concatenate((x,np.tile([0],(m+2)*(n+2)-(m*n))))
Py=np.concatenate((y,np.tile([0],(m+2)*(n+2)-(m*n))))
Pz=np.concatenate((z,np.tile([0],(m+2)*(n+2)-(m*n))))
# passing matrix with free end conditions
phi=np.zeros(((n+2)*(m+2),(m+2)*(n+2)))
# interpolation equations 
for j in range(m):
    for i in range(n):
        phi[i+(j)*n,i+(j)*(n+2)]=1
        phi[i+(j)*n,i+(j)*(n+2)+1]=4
        phi[i+(j)*n,i+(j)*(n+2)+2]=1
        phi[i+(j)*n,i+(j+1)*(n+2)]=4
        phi[i+(j)*n,i+(j+1)*(n+2)+1]=16
        phi[i+(j)*n,i+(j+1)*(n+2)+2]=4
        phi[i+(j)*n,i+(j+2)*(n+2)]=1
        phi[i+(j)*n,i+(j+2)*(n+2)+1]=4
        phi[i+(j)*n,i+(j+2)*(n+2)+2]=1        
# dS/du=0 at x- border     
for i in range(0,m+2):
    phi[n*m+i,(i*(n+2))%((n+2)*(m+2))]=phi[n*m+i,(i*(n+2))%((n+2)*(m+2))]-3
    phi[n*m+i,(i*(n+2)+2)%((n+2)*(m+2))]=phi[n*m+i,(i*(n+2)+2)%((n+2)*(m+2))]+3
    phi[n*m+i,((i+1)*(n+2))%((n+2)*(m+2))]=phi[n*m+i,((i+1)*(n+2))%((n+2)*(m+2))]-12
    phi[n*m+i,((i+1)*(n+2)+2)%((n+2)*(m+2))]=phi[n*m+i,((i+1)*(n+2)+2)%((n+2)*(m+2))]+12
    phi[n*m+i,((i+2)*(n+2))%((n+2)*(m+2))]=phi[n*m+i,((i+2)*(n+2))%((n+2)*(m+2))]-3
    phi[n*m+i,((i+2)*(n+2)+2)%((n+2)*(m+2))]=phi[n*m+i,((i+2)*(n+2)+2)%((n+2)*(m+2))]+3 
# dS/du=0 at x+ border   
for i in range(0,m+2):
    phi[n*m+i+m+2,((i+1)*(n+2)-1)%((n+2)*(m+2))]=phi[n*m+i+m+2,((i+1)*(n+2)-1)%((n+2)*(m+2))]-3
    phi[n*m+i+m+2,((i+1)*(n+2)-3)%((n+2)*(m+2))]=phi[n*m+i+m+2,((i+1)*(n+2)-3)%((n+2)*(m+2))]+3
    phi[n*m+i+m+2,((i+2)*(n+2)-1)%((n+2)*(m+2))]=phi[n*m+i+m+2,((i+2)*(n+2)-1)%((n+2)*(m+2))]-12
    phi[n*m+i+m+2,((i+2)*(n+2)-3)%((n+2)*(m+2))]=phi[n*m+i+m+2,((i+2)*(n+2)-3)%((n+2)*(m+2))]+12
    phi[n*m+i+m+2,((i+3)*(n+2)-1)%((n+2)*(m+2))]=phi[n*m+i+m+2,((i+3)*(n+2)-1)%((n+2)*(m+2))]-3
    phi[n*m+i+m+2,((i+3)*(n+2)-3)%((n+2)*(m+2))]=phi[n*m+i+m+2,((i+3)*(n+2)-3)%((n+2)*(m+2))]+3     
# dS/du between y+ and y- borders  
for i in range(0,n):
    phi[n*m+2*(m+2)+i,i]=-3
    phi[n*m+2*(m+2)+i,i+1]=-12
    phi[n*m+2*(m+2)+i,i+2]=-3
    phi[n*m+2*(m+2)+i,2*(n+2)+i]=3
    phi[n*m+2*(m+2)+i,2*(n+2)+i+1]=12
    phi[n*m+2*(m+2)+i,2*(n+2)+i+2]=3
    phi[n*m+2*(m+2)+i,(m-1)*(n+2)+i]=3
    phi[n*m+2*(m+2)+i,(m-1)*(n+2)+i+1]=12
    phi[n*m+2*(m+2)+i,(m-1)*(n+2)+i+2]=3
    phi[n*m+2*(m+2)+i,(m+1)*(n+2)+i]=-3
    phi[n*m+2*(m+2)+i,(m+1)*(n+2)+i+1]=-12
    phi[n*m+2*(m+2)+i,(m+1)*(n+2)+i+2]=-3
# d2S/du2 between y+ and y- borders
for i in range(n):
    phi[n*m+2*(m+2)+n+i,i]=6
    phi[n*m+2*(m+2)+n+i,i+1]=24
    phi[n*m+2*(m+2)+n+i,i+2]=6
    phi[n*m+2*(m+2)+n+i,(n+2)+i]=-12
    phi[n*m+2*(m+2)+n+i,(n+2)+i+1]=-48    
    phi[n*m+2*(m+2)+n+i,(n+2)+i+2]=-12
    phi[n*m+2*(m+2)+n+i,2*(n+2)+i]=6
    phi[n*m+2*(m+2)+n+i,2*(n+2)+i+1]=24    
    phi[n*m+2*(m+2)+n+i,2*(n+2)+i+2]=6 
    phi[n*m+2*(m+2)+n+i,(m-1)*(n+2)+i]=-6
    phi[n*m+2*(m+2)+n+i,(m-1)*(n+2)+i+1]=-24   
    phi[n*m+2*(m+2)+n+i,(m-1)*(n+2)+i+2]=-6
    phi[n*m+2*(m+2)+n+i,(m)*(n+2)+i]=12
    phi[n*m+2*(m+2)+n+i,(m)*(n+2)+i+1]=48    
    phi[n*m+2*(m+2)+n+i,(m)*(n+2)+i+2]=12
    phi[n*m+2*(m+2)+n+i,(m+1)*(n+2)+i]=-6
    phi[n*m+2*(m+2)+n+i,(m+1)*(n+2)+i+1]=-24    
    phi[n*m+2*(m+2)+n+i,(m+1)*(n+2)+i+2]=-6 
# control points 
phi_inv=np.linalg.inv(phi)
Qx=36*phi_inv.dot(Px)
Qy=36*phi_inv.dot(Py)
Qz=36*phi_inv.dot(Pz)
# figure plot
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z,color='black')
t=9 # patch discretization
U=np.linspace(0,1,num=t)
V=np.linspace(0,1,num=t)
u,v = np.meshgrid(U, V)
for pv in range(0,n-1):
    for pu in range (0,m-1):
        V1=(1-v)**3
        V2=3*v**3-6*v**2+4
        V3=-3*v**3+3*v**2+3*v+1
        V4=v**3
        U1=(1-u)**3    
        U2=3*u**3-6*u**2+4
        U3=-3*u**3+3*u**2+3*u+1
        U4=u**3
        param_x=((V1*(Qx[pv+pu*(n+2)]*U1+Qx[pv+n+2+pu*(n+2)]*U2+Qx[pv+2*(n+2)+pu*(n+2)]*U3+Qx[pv+3*(n+2)+pu*(n+2)]*U4)) \
        		+(V2*(Qx[pv+1+pu*(n+2)]*U1+Qx[pv+1+n+2+pu*(n+2)]*U2+Qx[pv+1+2*(n+2)+pu*(n+2)]*U3+Qx[pv+1+3*(n+2)+pu*(n+2)]*U4)) \
        		+(V3*(Qx[pv+2+pu*(n+2)]*U1+Qx[pv+2+n+2+pu*(n+2)]*U2+Qx[pv+2+2*(n+2)+pu*(n+2)]*U3+Qx[pv+2+3*(n+2)+pu*(n+2)]*U4)) \
        		+(V4*(Qx[pv+3+pu*(n+2)]*U1+Qx[pv+3+n+2+pu*(n+2)]*U2+Qx[pv+3+2*(n+2)+pu*(n+2)]*U3+Qx[pv+3+3*(n+2)+pu*(n+2)]*U4)))/36;
        param_y=((V1*(Qy[pv+pu*(n+2)]*U1+Qy[pv+n+2+pu*(n+2)]*U2+Qy[pv+2*(n+2)+pu*(n+2)]*U3+Qy[pv+3*(n+2)+pu*(n+2)]*U4)) \
        		+(V2*(Qy[pv+1+pu*(n+2)]*U1+Qy[pv+1+n+2+pu*(n+2)]*U2+Qy[pv+1+2*(n+2)+pu*(n+2)]*U3+Qy[pv+1+3*(n+2)+pu*(n+2)]*U4)) \
        		+(V3*(Qy[pv+2+pu*(n+2)]*U1+Qy[pv+2+n+2+pu*(n+2)]*U2+Qy[pv+2+2*(n+2)+pu*(n+2)]*U3+Qy[pv+2+3*(n+2)+pu*(n+2)]*U4)) \
        		+(V4*(Qy[pv+3+pu*(n+2)]*U1+Qy[pv+3+n+2+pu*(n+2)]*U2+Qy[pv+3+2*(n+2)+pu*(n+2)]*U3+Qy[pv+3+3*(n+2)+pu*(n+2)]*U4)))/36;      
        param_z=((V1*(Qz[pv+pu*(n+2)]*U1+Qz[pv+n+2+pu*(n+2)]*U2+Qz[pv+2*(n+2)+pu*(n+2)]*U3+Qz[pv+3*(n+2)+pu*(n+2)]*U4)) \
        		+(V2*(Qz[pv+1+pu*(n+2)]*U1+Qz[pv+1+n+2+pu*(n+2)]*U2+Qz[pv+1+2*(n+2)+pu*(n+2)]*U3+Qz[pv+1+3*(n+2)+pu*(n+2)]*U4)) \
        		+(V3*(Qz[pv+2+pu*(n+2)]*U1+Qz[pv+2+n+2+pu*(n+2)]*U2+Qz[pv+2+2*(n+2)+pu*(n+2)]*U3+Qz[pv+2+3*(n+2)+pu*(n+2)]*U4)) \
        		+(V4*(Qz[pv+3+pu*(n+2)]*U1+Qz[pv+3+n+2+pu*(n+2)]*U2+Qz[pv+3+2*(n+2)+pu*(n+2)]*U3+Qz[pv+3+3*(n+2)+pu*(n+2)]*U4)))/36;
        ax.plot_surface(param_x,param_y,param_z,color='orange',alpha=0.9) 
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.savefig('bicubic_parametric_sphere.png')
